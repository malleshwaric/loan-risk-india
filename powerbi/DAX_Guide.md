# Power BI & DAX Guide — Bank Loan & Credit Risk Analytics (India)

This guide walks through building the Power BI report on top of the five CSVs in `/data`.

## 1. Data Model

Import all 5 tables (`branches`, `loan_products`, `customers`, `loan_applications`, `loan_repayments`) and build this star-ish schema:

```
customers (1) ──< loan_applications >── (1) branches
                        │
                        ├──< (1) loan_products
                        │
                        └──< (many) loan_repayments
```

Relationships:
- `customers[customer_id]` 1 → many `loan_applications[customer_id]`
- `branches[branch_id]` 1 → many `loan_applications[branch_id]`
- `loan_products[product_id]` 1 → many `loan_applications[product_id]`
- `loan_applications[application_id]` 1 → many `loan_repayments[application_id]`

Also add a **Date table** (Power Query → New Source → Blank Query) spanning `application_date` min to today, marked as a Date Table, and relate it to `loan_applications[application_date]` and `loan_repayments[due_date]` (use the date table for the applications relationship as active; mark the repayments one inactive and use `USERELATIONSHIP` where needed).

## 2. Key DAX Measures

### Portfolio & Volume
```dax
Total Applications = COUNTROWS(loan_applications)

Total Approved Loans =
CALCULATE(COUNTROWS(loan_applications), loan_applications[application_status] = "Approved")

Approval Rate % =
DIVIDE([Total Approved Loans], [Total Applications], 0)

Total Disbursed Amount =
CALCULATE(SUM(loan_applications[loan_amount_approved]), loan_applications[application_status] = "Approved")

Avg Loan Size =
DIVIDE([Total Disbursed Amount], [Total Approved Loans], 0)
```

### Risk & Default
```dax
Total Defaulted Loans =
CALCULATE(COUNTROWS(loan_applications), loan_applications[loan_status] = "Defaulted")

Default Rate % =
DIVIDE([Total Defaulted Loans], [Total Approved Loans], 0)

NPA Exposure =
CALCULATE(
    SUM(loan_applications[loan_amount_approved]),
    loan_applications[loan_status] IN {"Defaulted", "Written-Off"}
)

NPA % =
DIVIDE([NPA Exposure], [Total Disbursed Amount], 0)

High Risk Loan Count =
CALCULATE(COUNTROWS(loan_applications), loan_applications[risk_category] = "High")
```

### Credit & Affordability
```dax
Avg Credit Score =
AVERAGE(customers[credit_score])

EMI to Income Ratio =
VAR TotalEMI = customers[existing_emi_monthly] + SELECTEDVALUE(loan_applications[emi_amount])
RETURN DIVIDE(TotalEMI * 12, customers[annual_income], 0)

High Debt Burden Customers =
CALCULATE(
    DISTINCTCOUNT(customers[customer_id]),
    FILTER(
        customers,
        DIVIDE(customers[existing_emi_monthly] * 12, customers[annual_income], 0) > 0.5
    )
)
```

### Repayment Behavior
```dax
On-Time Payment % =
DIVIDE(
    CALCULATE(COUNTROWS(loan_repayments), loan_repayments[payment_status] = "On-Time"),
    COUNTROWS(loan_repayments), 0
)

Missed Payment Count =
CALCULATE(COUNTROWS(loan_repayments), loan_repayments[payment_status] = "Missed")

Avg Days Late =
CALCULATE(AVERAGE(loan_repayments[days_late]), loan_repayments[payment_status] = "Late")
```

### Time Intelligence
```dax
Disbursed Amount MTD =
TOTALMTD([Total Disbursed Amount], 'Date'[Date])

Disbursed Amount YoY % =
VAR Prior = CALCULATE([Total Disbursed Amount], SAMEPERIODLASTYEAR('Date'[Date]))
RETURN DIVIDE([Total Disbursed Amount] - Prior, Prior, 0)
```

## 3. Calculated Columns

```dax
-- Age bracket for customers
Age Bracket =
VAR Age = DATEDIFF(customers[date_of_birth], TODAY(), YEAR)
RETURN
    SWITCH(
        TRUE(),
        Age < 25, "18-24",
        Age < 35, "25-34",
        Age < 45, "35-44",
        Age < 55, "45-54",
        "55+"
    )

-- Credit score band
Credit Score Band =
SWITCH(
    TRUE(),
    customers[credit_score] >= 800, "Excellent (800+)",
    customers[credit_score] >= 750, "Very Good (750-799)",
    customers[credit_score] >= 700, "Good (700-749)",
    customers[credit_score] >= 650, "Fair (650-699)",
    "Poor (<650)"
)
```

## 4. Suggested Report Pages

1. **Portfolio Overview** — KPI cards (Total Disbursed, Approval Rate, Avg Loan Size, NPA %), trend line of monthly disbursal, product mix donut.
2. **Risk & Default Analysis** — Default rate by risk category and credit score band, NPA exposure by branch/zone (map or bar), high-risk customer table.
3. **Customer & Affordability** — Income vs loan amount scatter, EMI-to-income distribution, occupation-type breakdown, age bracket analysis.
4. **Repayment Behavior** — On-time vs late vs missed trend, days-late distribution, occupation-type repayment comparison.
5. **Branch Performance** — Branch/zone scorecards: applications, approval rate, NPA %, portfolio value (use a matrix visual with conditional formatting).

## 5. Design Notes

- Use a conditional-formatting red/amber/green scale on Risk Category and NPA % columns to make problem areas pop immediately.
- Add a Credit Score Band slicer and Date range slicer on every page for consistent filtering.
- For the branch map, use `Map` or `Filled Map` visual keyed on `state`/`city` (Power BI will geocode Indian city names automatically in most cases — verify a few manually).
