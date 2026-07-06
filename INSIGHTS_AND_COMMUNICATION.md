# Business Insights & Stakeholder Communication
## Bank Loan & Credit Risk Analytics — India

---

## 1. Business Context

### Who commissioned this analysis?
A mid-sized Indian retail bank with 55 branches across 5 zones wants to understand the health of its loan portfolio. The Head of Risk, CFO, and Branch Operations team are the primary stakeholders.

### What problem are we solving?
The bank has seen rising NPA (Non-Performing Asset) levels and wants answers to three specific questions:
- Which customer segments and branches carry the most default risk?
- Are we pricing loans correctly for the risk we're taking?
- Where should we tighten underwriting without hurting business volume?

### Why does this matter financially?
With ₹9.67B disbursed and ₹1.09B in NPA exposure, the bank is carrying an **11.3% NPA ratio on its risky segments**. The RBI's comfort threshold is 5%. This is a board-level concern.

---

## 2. Key Findings

### Finding 1: High Risk loans default at nearly 10× the rate of Low Risk loans
- **Low Risk default rate:** 2.3%
- **Medium Risk default rate:** 8.5%
- **High Risk default rate:** 19.5%

**So what:** The bank is approving High Risk loans that default at nearly 1 in 5 cases. Either the risk scoring model is too lenient, or loan officers are overriding risk flags for business volume.

---

### Finding 2: The East zone carries the highest NPA exposure
- East zone NPA: ₹285M (26.1% of total NPA)
- South zone: ₹213M
- North zone: ₹208M
- West zone: ₹206M
- Central zone: ₹184M

**So what:** East zone branches are either serving a higher-risk customer base or have weaker underwriting practices. A branch-level audit of East zone approval decisions is warranted.

---

### Finding 3: Home Loans dominate the portfolio but carry concentrated risk
- Home Loans = 36.5% of disbursed amount (₹3.53B)
- Any systemic shock to residential real estate will impact over a third of the portfolio

**So what:** The portfolio is under-diversified. Increasing the share of Gold Loans (secured, lower default risk) and reducing Home Loan concentration would reduce portfolio volatility.

---

### Finding 4: 62.6% approval rate — 37.4% of applicants are being rejected
- Top rejection reasons: Low Credit Score, High Debt-to-Income Ratio, Incomplete Documentation

**So what:** One-third of applicants are rejected. If "Incomplete Documentation" is a top reason, the bank is losing potentially creditworthy customers due to a process problem, not a risk problem. Digitising document collection could recover 5–8% of rejected applications.

---

### Finding 5: On-Time Payment rate is 79.5% — lower than industry benchmark
- Industry benchmark for on-time payments in Indian retail banking: ~85–88%
- Business Owners have the lowest on-time rates; Self-Employed the highest

**So what:** There's a 5–8 percentage point gap versus benchmark. Automated EMI reminders 3–5 days before due dates could close this gap significantly.

---

### Finding 6: Credit scores are clustered around 700 — the "gray zone"
- Average credit score: 698.9 (CIBIL scale 300–900)
- This is right at the boundary between "fair" and "good" credit

**So what:** The bank is heavily exposed to borderline borrowers. A more granular risk pricing strategy (charge higher interest for 650–720 vs 720+ scores) would improve risk-adjusted returns without reducing approval volume.

---

## 3. Business Recommendations

| Priority | Recommendation | Expected Impact |
|---|---|---|
| 🔴 High | Cap High Risk loan approvals at 15% of monthly disbursals | Reduce NPA by estimated 3–4% |
| 🔴 High | Audit East zone branch underwriting — retrain loan officers | Address 26% of NPA concentration |
| 🟠 Medium | Introduce risk-based pricing — higher rates for 650–720 CIBIL | Improve margin on risky loans by ~1.5% |
| 🟠 Medium | Automate EMI reminders via SMS/WhatsApp 3 days before due date | Improve on-time rate from 79.5% to ~84% |
| 🟡 Low | Digitise document submission — reduce "Incomplete Documentation" rejections | Recover ~5% of rejected applications |
| 🟡 Low | Rebalance portfolio — grow Gold Loan share from 6.1% to 10% | Reduce Home Loan concentration risk |

---

## 4. Stakeholder Presentation Script

### Opening (30 seconds — for a CFO or Head of Risk)
> "Good morning. I've completed a full analysis of our loan portfolio — ₹9.67 billion across 9,390 approved loans. I want to walk you through three things: where our NPA risk is concentrated, what's driving it, and what we can do about it. The headline is that our High Risk segment is defaulting at nearly 20%, and East zone branches account for over a quarter of our total NPA exposure. There are four targeted actions that could bring our NPA ratio below the RBI threshold within two quarters."

---

### Walking through the data (for a 15-minute stakeholder meeting)

**Slide 1 — Portfolio Snapshot (2 minutes)**
> "At a portfolio level, we've disbursed ₹9.67B across 9,390 approved loans. Our approval rate is 62.6% — healthy. Average loan size is ₹10.3 lakhs. The concern is our default rate at 7.9% and NPA exposure at ₹1.09B — that's 11.3% of disbursed value sitting in stressed assets."

**Slide 2 — The Risk Segmentation Problem (3 minutes)**
> "When we break down defaults by our own risk categories, it's stark. Low Risk customers default at 2.3% — that's acceptable. Medium Risk is 8.5% — manageable. But High Risk is defaulting at 19.5%. One in five High Risk loans is failing. The question is: why are we approving them? Either our risk model is miscalibrated, or we're overriding it for volume targets. I'd recommend we look at the approval trail for High Risk loans in the last 6 months."

**Slide 3 — Geographic Concentration (3 minutes)**
> "East zone is our biggest concern geographically. It holds ₹285M in NPA — 26% of our total stressed assets. That's nearly 80% more than Central zone. When I drilled into East zone, the approval rate is actually slightly higher than other zones at 63.5%. That suggests it's not a demand problem — it's an underwriting problem. East zone branches may be approving applicants that other zones would reject."

**Slide 4 — The Repayment Gap (3 minutes)**
> "Our on-time payment rate is 79.5%. Industry benchmark is 85–88%. That's a real gap. The good news is it's uniform across occupation types — all segments are in the 79–80% range — which tells me this isn't a segment problem. It's a process problem. Customers aren't defaulting intentionally; they're missing EMIs because they forget. An automated reminder system is a low-cost, high-return fix."

**Slide 5 — Recommendations (4 minutes)**
> "My four recommendations in priority order: One, cap High Risk approvals at 15% of monthly disbursals immediately. Two, audit East zone underwriting practices — I've identified the specific branches with above-average NPA ratios. Three, implement risk-based pricing for the 650–720 CIBIL band — we're charging these customers the same rates as 750+ customers, which isn't justified by the risk. Four, deploy automated EMI reminders — our data shows 15.5% of payments are late, not missed — these customers intend to pay, they just need a nudge."

---

### Handling pushback

**Q: "Our approval rates are already lower than competitors — won't capping High Risk hurt volume?"**
> "Fair concern. But consider: a High Risk loan that defaults destroys 5–7 years of interest income. At 19.5% default rate, every 5 High Risk loans approved costs us the equivalent of 1 complete writeoff. We're not turning away volume — we're protecting the margin on the volume we do approve."

**Q: "The East zone has our biggest growth market. Can we really pull back there?"**
> "We're not recommending pulling back on volume — we're recommending fixing underwriting quality. The East zone can still grow disbursals; the goal is to grow them with better-quality borrowers. The data shows the issue is with specific High Risk approvals, not the market itself."

**Q: "Why is on-time payment rate the metric to focus on? NPA is the real number."**
> "On-time payments are a leading indicator of NPA — they're 6–12 months earlier in the signal chain. If we fix the on-time rate now, we prevent next year's NPA. By the time a loan shows as NPA, the loss is already locked in."

---

## 5. Interview Talking Points

### How to describe this project in an interview

**The 60-second version:**
> "I did a full credit risk analysis of a retail bank loan portfolio across India — 6,000 customers, 15,000 loan applications, 150,000 repayment records across 55 branches. The data covers the full lending lifecycle from application through disbursal and monthly repayment. I built the SQL schema from scratch, handled all the data prep in Python, and built a 5-page Power BI report across portfolio overview, risk segmentation, repayment behaviour, branch performance, and customer analysis. The headline finding is that High Risk loans default at 19.5% versus 2.3% for Low Risk — and East zone branches carry 26% of total NPA exposure despite having higher approval rates, which points to an underwriting quality issue rather than a market problem."

**Key metrics to memorise:**
- ₹9.67B total portfolio
- 62.6% approval rate
- 7.9% default rate
- 19.5% High Risk default rate vs 2.3% Low Risk
- ₹1.09B NPA exposure
- 79.5% on-time payment rate
- East zone = 26.1% of total NPA

**Technical questions you might be asked:**

*"How did you structure the credit risk data model?"*
> "Approval probability is driven by CIBIL score — the relationship is (score - 300) / 600, scaled and clipped to 5–95%. This creates a natural gradient where 750+ scores hit ~85% approval and sub-650 scores drop to ~30%. Risk category is assigned conditionally on score, and default probability is a direct function of risk category. So the key relationships — credit score → risk category → default rate — are internally consistent throughout the dataset."

*"What DAX measures did you use for NPA?"*
> "NPA Exposure = CALCULATE(SUM(loan_applications[loan_amount_approved]), loan_applications[loan_status] IN {'Defaulted', 'Written-Off'}). I also calculated NPA % as DIVIDE([NPA Exposure], [Total Disbursed Amount], 0), which lets you slice NPA concentration by any dimension — branch, zone, product, risk category."

*"What would you do differently with real bank data?"*
> "With real data I'd add vintage analysis — tracking default rates by origination month to detect underwriting standard drift over time. I'd also model Loss Given Default (LGD) by including collateral values for secured loans like Home and Gold Loans, which changes the risk picture significantly compared to unsecured Personal Loans."
