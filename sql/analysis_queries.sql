-- Bank Loan & Credit Risk Analytics (India)
-- Analysis Queries


-- 1. Overall approval rate by loan product
SELECT
    lp.product_name,
    COUNT(*) AS total_applications,
    SUM(CASE WHEN la.application_status = 'Approved' THEN 1 ELSE 0 END) AS approved_count,
    ROUND(SUM(CASE WHEN la.application_status = 'Approved' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS approval_rate_pct
FROM loan_applications la
JOIN loan_products lp ON la.product_id = lp.product_id
GROUP BY lp.product_name
ORDER BY approval_rate_pct DESC;

-- 2. Default rate by risk category
SELECT
    risk_category,
    COUNT(*) AS total_loans,
    SUM(CASE WHEN loan_status = 'Defaulted' THEN 1 ELSE 0 END) AS defaulted_loans,
    ROUND(SUM(CASE WHEN loan_status = 'Defaulted' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS default_rate_pct
FROM loan_applications
WHERE application_status = 'Approved'
GROUP BY risk_category
ORDER BY default_rate_pct DESC;

-- 3. Average credit score vs default outcome
SELECT
    c.credit_score / 50 * 50 AS credit_score_band,
    COUNT(*) AS loan_count,
    SUM(CASE WHEN la.loan_status = 'Defaulted' THEN 1 ELSE 0 END) AS defaults,
    ROUND(AVG(la.loan_amount_approved), 2) AS avg_loan_amount
FROM loan_applications la
JOIN customers c ON la.customer_id = c.customer_id
WHERE la.application_status = 'Approved'
GROUP BY credit_score_band
ORDER BY credit_score_band;

-- 4. Branch-wise NPA (Non-Performing Asset) exposure
SELECT
    b.branch_name,
    b.state,
    b.zone,
    COUNT(la.application_id) AS total_loans,
    SUM(CASE WHEN la.loan_status IN ('Defaulted','Written-Off') THEN la.loan_amount_approved ELSE 0 END) AS npa_exposure,
    ROUND(SUM(CASE WHEN la.loan_status IN ('Defaulted','Written-Off') THEN la.loan_amount_approved ELSE 0 END)
        / NULLIF(SUM(la.loan_amount_approved),0) * 100, 2) AS npa_pct
FROM loan_applications la
JOIN branches b ON la.branch_id = b.branch_id
WHERE la.application_status = 'Approved'
GROUP BY b.branch_name, b.state, b.zone
ORDER BY npa_pct DESC;

-- 5. EMI-to-income ratio risk flag (debt burden analysis)
SELECT
    c.customer_id,
    c.full_name,
    c.annual_income,
    c.existing_emi_monthly,
    la.emi_amount,
    ROUND((c.existing_emi_monthly + la.emi_amount) * 12 / NULLIF(c.annual_income,0) * 100, 2) AS total_emi_to_income_pct,
    CASE
        WHEN (c.existing_emi_monthly + la.emi_amount) * 12 / NULLIF(c.annual_income,0) > 0.5 THEN 'High Risk'
        WHEN (c.existing_emi_monthly + la.emi_amount) * 12 / NULLIF(c.annual_income,0) > 0.35 THEN 'Medium Risk'
        ELSE 'Low Risk'
    END AS debt_burden_flag
FROM loan_applications la
JOIN customers c ON la.customer_id = c.customer_id
WHERE la.application_status = 'Approved'
ORDER BY total_emi_to_income_pct DESC
LIMIT 100;

-- 6. Monthly disbursal trend (loan amount disbursed over time)
SELECT
    DATE_FORMAT(disbursal_date, '%Y-%m') AS disbursal_month,
    COUNT(*) AS loans_disbursed,
    SUM(loan_amount_approved) AS total_disbursed_amount,
    ROUND(AVG(loan_amount_approved), 2) AS avg_loan_size
FROM loan_applications
WHERE disbursal_date IS NOT NULL
GROUP BY disbursal_month
ORDER BY disbursal_month;

-- 7. Late payment behavior by occupation type
SELECT
    c.occupation_type,
    COUNT(lr.repayment_id) AS total_repayments,
    SUM(CASE WHEN lr.payment_status = 'Late' THEN 1 ELSE 0 END) AS late_payments,
    SUM(CASE WHEN lr.payment_status = 'Missed' THEN 1 ELSE 0 END) AS missed_payments,
    ROUND(AVG(lr.days_late), 1) AS avg_days_late
FROM loan_repayments lr
JOIN loan_applications la ON lr.application_id = la.application_id
JOIN customers c ON la.customer_id = c.customer_id
GROUP BY c.occupation_type
ORDER BY missed_payments DESC;

-- 8. Top rejection reasons
SELECT
    rejection_reason,
    COUNT(*) AS rejection_count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM loan_applications WHERE application_status = 'Rejected'), 2) AS pct_of_rejections
FROM loan_applications
WHERE application_status = 'Rejected'
GROUP BY rejection_reason
ORDER BY rejection_count DESC;

-- 9. Zone-wise portfolio summary
SELECT
    b.zone,
    COUNT(la.application_id) AS total_loans,
    SUM(la.loan_amount_approved) AS total_portfolio_value,
    ROUND(AVG(c.credit_score), 0) AS avg_credit_score,
    ROUND(SUM(CASE WHEN la.loan_status = 'Defaulted' THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS default_rate_pct
FROM loan_applications la
JOIN branches b ON la.branch_id = b.branch_id
JOIN customers c ON la.customer_id = c.customer_id
WHERE la.application_status = 'Approved'
GROUP BY b.zone
ORDER BY total_portfolio_value DESC;

-- 10. Customer tenure vs loyalty (repeat borrowers)
SELECT
    c.customer_id,
    c.full_name,
    c.bank_relationship_years,
    COUNT(la.application_id) AS total_loans_taken,
    SUM(la.loan_amount_approved) AS lifetime_loan_value
FROM customers c
JOIN loan_applications la ON c.customer_id = la.customer_id
WHERE la.application_status = 'Approved'
GROUP BY c.customer_id, c.full_name, c.bank_relationship_years
HAVING COUNT(la.application_id) > 1
ORDER BY lifetime_loan_value DESC;
