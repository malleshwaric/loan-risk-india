# Bank Loan & Credit Risk Analytics — India

End-to-end data analytics project simulating a retail bank's loan portfolio across India: applications, approvals, disbursals, repayments, and default/NPA risk. Built to demonstrate SQL data modeling, Python data generation, and Power BI/DAX reporting skills for a Data Analyst portfolio.

## Project Overview

A bank wants to understand:
- Where loan applications are coming from, and what's getting approved vs rejected
- Which customer segments and branches carry the highest default/NPA risk
- How credit score, income, and existing debt burden predict repayment behavior
- Repayment performance (on-time / late / missed) across customer occupation types

This project builds a realistic relational dataset and a full analytics layer (SQL queries + Power BI dashboard plan) to answer those questions.

## Tech Stack

- **Python** (pandas, numpy, faker) — synthetic data generation
- **SQL** (MySQL/PostgreSQL-compatible) — schema design + analysis queries
- **Power BI** — DAX measures and dashboard design guide

## Repository Structure

```
loan-risk-india/
├── data/                       # Generated CSVs (output of generate_data.py)
│   ├── branches.csv
│   ├── loan_products.csv
│   ├── customers.csv
│   ├── loan_applications.csv
│   └── loan_repayments.csv
├── python/
│   └── generate_data.py        # Synthetic data generator
├── sql/
│   ├── schema.sql               # Table definitions + indexes
│   └── analysis_queries.sql     # 10 business analysis queries
├── powerbi/
│   └── DAX_Guide.md             # Data model, DAX measures, report page layout
└── README.md
```

## Data Model

5 tables, ~6,000 customers, ~15,000 loan applications, ~150,000 repayment records:

- **branches** — 55 branches across 5 zones (North/South/East/West/Central) and 4 city tiers
- **loan_products** — Home, Personal, Auto, Education, Gold, Business loans with realistic Indian interest rate ranges
- **customers** — demographics, income, CIBIL-style credit score (300–900), occupation type
- **loan_applications** — the core fact table: requested/approved amount, tenure, EMI, status, risk category, loan outcome
- **loan_repayments** — monthly installment-level repayment history with on-time/late/missed status

Approval probability, risk category, and default likelihood are all modeled as functions of credit score, so the dataset behaves the way a real credit risk dataset would (higher score → higher approval, lower default).

## How to Run

```bash
# 1. Generate the data
cd python
pip install faker numpy pandas
python generate_data.py

# 2. Load into your SQL engine of choice
mysql -u youruser -p yourdb < ../sql/schema.sql
# then load the CSVs from /data using LOAD DATA INFILE or your DB's import tool

# 3. Run analysis queries
mysql -u youruser -p yourdb < ../sql/analysis_queries.sql

# 4. Power BI
# Import the 5 CSVs directly, or connect to your SQL database.
# Follow powerbi/DAX_Guide.md for the data model, measures, and report layout.
```

## Key Analysis Questions Answered

1. What's the approval rate by loan product?
2. How does default rate vary by risk category and credit score band?
3. Which branches/zones carry the highest NPA exposure?
4. Which customers are over-leveraged (high EMI-to-income ratio)?
5. What are the most common rejection reasons?
6. How does repayment discipline differ by occupation type?
7. What does the monthly disbursal trend look like?
8. Who are the repeat/loyal borrowers by lifetime loan value?

See `sql/analysis_queries.sql` for the full query set.

## Sample Insights (from generated data)

- ~63% overall approval rate, varying significantly by product type and credit score band
- Default rate climbs sharply for "High" risk category loans vs "Low" risk
- EMI-to-income ratio above 50% is a strong leading indicator of repayment stress
- Salaried customers show the most consistent on-time repayment behavior vs self-employed/business owners

## Author

Malleshwari C — Data Analyst portfolio project. See related projects: [ShopKart India](../shopkart-india), [SwiftMove India](../swiftmove-india).
