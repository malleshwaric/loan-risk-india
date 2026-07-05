"""
Bank Loan & Credit Risk Analytics (India)
Synthetic Data Generator

Generates realistic, internally-consistent CSV data for:
branches, loan_products, customers, loan_applications, loan_repayments

Usage:
    pip install faker numpy pandas
    python generate_data.py
"""

import random
import numpy as np
import pandas as pd
from datetime import date, timedelta
from faker import Faker

fake = Faker("en_IN")
random.seed(42)
np.random.seed(42)

OUTPUT_DIR = "data"
import os
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ------------------------------------------------------------
# 1. Branches
# ------------------------------------------------------------
CITIES_BY_ZONE = {
    "North": [("Delhi", "Delhi"), ("Chandigarh", "Chandigarh"), ("Lucknow", "Uttar Pradesh"), ("Jaipur", "Rajasthan")],
    "South": [("Bengaluru", "Karnataka"), ("Chennai", "Tamil Nadu"), ("Hyderabad", "Telangana"), ("Kochi", "Kerala")],
    "East":  [("Kolkata", "West Bengal"), ("Patna", "Bihar"), ("Bhubaneswar", "Odisha"), ("Guwahati", "Assam")],
    "West":  [("Mumbai", "Maharashtra"), ("Pune", "Maharashtra"), ("Ahmedabad", "Gujarat"), ("Surat", "Gujarat")],
    "Central": [("Bhopal", "Madhya Pradesh"), ("Nagpur", "Maharashtra"), ("Raipur", "Chhattisgarh")],
}
BRANCH_TYPES = ["Metro", "Urban", "Semi-Urban", "Rural"]

branches = []
branch_id = 1
for zone, cities in CITIES_BY_ZONE.items():
    for city, state in cities:
        for i in range(random.randint(2, 4)):
            branches.append({
                "branch_id": branch_id,
                "branch_name": f"{city} Branch {i+1}",
                "city": city,
                "state": state,
                "zone": zone,
                "branch_type": random.choices(BRANCH_TYPES, weights=[0.3, 0.35, 0.25, 0.1])[0],
                "opened_date": fake.date_between(start_date="-15y", end_date="-1y"),
            })
            branch_id += 1

branches_df = pd.DataFrame(branches)
branches_df.to_csv(f"{OUTPUT_DIR}/branches.csv", index=False)

# ------------------------------------------------------------
# 2. Loan products
# ------------------------------------------------------------
loan_products = [
    {"product_id": 1, "product_name": "Home Loan", "interest_type": "Floating", "min_interest_rate": 8.4, "max_interest_rate": 10.5, "min_tenure_months": 60, "max_tenure_months": 360, "processing_fee_pct": 0.5},
    {"product_id": 2, "product_name": "Personal Loan", "interest_type": "Fixed", "min_interest_rate": 10.5, "max_interest_rate": 18.0, "min_tenure_months": 12, "max_tenure_months": 60, "processing_fee_pct": 2.0},
    {"product_id": 3, "product_name": "Auto Loan", "interest_type": "Fixed", "min_interest_rate": 8.8, "max_interest_rate": 12.5, "min_tenure_months": 12, "max_tenure_months": 84, "processing_fee_pct": 1.0},
    {"product_id": 4, "product_name": "Education Loan", "interest_type": "Floating", "min_interest_rate": 9.0, "max_interest_rate": 12.0, "min_tenure_months": 60, "max_tenure_months": 180, "processing_fee_pct": 0.75},
    {"product_id": 5, "product_name": "Gold Loan", "interest_type": "Fixed", "min_interest_rate": 7.5, "max_interest_rate": 11.0, "min_tenure_months": 6, "max_tenure_months": 36, "processing_fee_pct": 0.5},
    {"product_id": 6, "product_name": "Business Loan", "interest_type": "Floating", "min_interest_rate": 11.0, "max_interest_rate": 16.5, "min_tenure_months": 12, "max_tenure_months": 120, "processing_fee_pct": 1.5},
]
loan_products_df = pd.DataFrame(loan_products)
loan_products_df.to_csv(f"{OUTPUT_DIR}/loan_products.csv", index=False)

# ------------------------------------------------------------
# 3. Customers
# ------------------------------------------------------------
N_CUSTOMERS = 6000
OCCUPATIONS = ["Salaried", "Self-Employed", "Business Owner", "Retired"]
OCC_WEIGHTS = [0.55, 0.2, 0.18, 0.07]

customers = []
all_cities = [(c, s) for cities in CITIES_BY_ZONE.values() for c, s in cities]

for cid in range(1, N_CUSTOMERS + 1):
    occupation = random.choices(OCCUPATIONS, weights=OCC_WEIGHTS)[0]
    city, state = random.choice(all_cities)
    dob = fake.date_of_birth(minimum_age=22, maximum_age=65)

    if occupation == "Salaried":
        income = np.random.lognormal(mean=13.1, sigma=0.45)
    elif occupation == "Self-Employed":
        income = np.random.lognormal(mean=13.0, sigma=0.6)
    elif occupation == "Business Owner":
        income = np.random.lognormal(mean=13.5, sigma=0.7)
    else:
        income = np.random.lognormal(mean=12.6, sigma=0.4)
    income = round(min(max(income, 180000), 9000000), -3)

    credit_score = int(np.clip(np.random.normal(700, 95), 300, 900))
    existing_emi = round(max(0, np.random.normal(income * 0.08 / 12, 3000)), -2) if random.random() < 0.4 else 0

    customers.append({
        "customer_id": cid,
        "full_name": fake.name(),
        "gender": random.choices(["Male", "Female"], weights=[0.58, 0.42])[0],
        "date_of_birth": dob,
        "city": city,
        "state": state,
        "occupation_type": occupation,
        "annual_income": income,
        "credit_score": credit_score,
        "existing_emi_monthly": existing_emi,
        "bank_relationship_years": round(random.uniform(0.5, 18), 1),
        "signup_date": fake.date_between(start_date="-18y", end_date="-1m"),
    })

customers_df = pd.DataFrame(customers)
customers_df.to_csv(f"{OUTPUT_DIR}/customers.csv", index=False)

# ------------------------------------------------------------
# 4. Loan applications
# ------------------------------------------------------------
N_APPLICATIONS = 15000
REJECTION_REASONS = [
    "Low Credit Score", "High Debt-to-Income Ratio", "Insufficient Income",
    "Incomplete Documentation", "Existing Default History", "Unverifiable Employment"
]

applications = []
app_id = 1
for _ in range(N_APPLICATIONS):
    customer = customers_df.sample(1).iloc[0]
    branch = branches_df.sample(1).iloc[0]
    product = loan_products_df.sample(1).iloc[0]

    app_date = fake.date_between(start_date="-3y", end_date="today")

    # Loan amount scaled to product type and income
    if product["product_name"] == "Home Loan":
        requested = round(customer["annual_income"] * random.uniform(3, 6), -3)
    elif product["product_name"] == "Auto Loan":
        requested = round(random.uniform(300000, 1500000), -3)
    elif product["product_name"] == "Education Loan":
        requested = round(random.uniform(200000, 2500000), -3)
    elif product["product_name"] == "Gold Loan":
        requested = round(random.uniform(50000, 800000), -3)
    elif product["product_name"] == "Business Loan":
        requested = round(customer["annual_income"] * random.uniform(0.5, 3), -3)
    else:  # Personal Loan
        requested = round(random.uniform(50000, 1500000), -3)

    tenure = random.randint(product["min_tenure_months"], product["max_tenure_months"])

    # Approval probability driven by credit score & EMI burden
    score_factor = (customer["credit_score"] - 300) / 600
    approval_prob = np.clip(score_factor * 0.9 + 0.05, 0.05, 0.95)
    status = random.choices(["Approved", "Rejected", "Pending", "Withdrawn"],
                             weights=[approval_prob, (1 - approval_prob) * 0.7, 0.08, 0.05])[0]

    approved_amount = None
    interest_rate = None
    emi = None
    rejection_reason = None
    risk_category = None
    disbursal_date = None
    loan_status = "NA"

    if status == "Approved":
        approved_amount = round(requested * random.uniform(0.75, 1.0), -3)
        interest_rate = round(random.uniform(product["min_interest_rate"], product["max_interest_rate"]), 2)
        r = interest_rate / 1200
        emi = round(approved_amount * r * (1 + r) ** tenure / ((1 + r) ** tenure - 1), 2)

        if customer["credit_score"] >= 750:
            risk_category = random.choices(["Low", "Medium", "High"], weights=[0.75, 0.22, 0.03])[0]
        elif customer["credit_score"] >= 650:
            risk_category = random.choices(["Low", "Medium", "High"], weights=[0.35, 0.5, 0.15])[0]
        else:
            risk_category = random.choices(["Low", "Medium", "High"], weights=[0.1, 0.4, 0.5])[0]

        disbursal_date = app_date + timedelta(days=random.randint(3, 21))

        default_prob = {"Low": 0.02, "Medium": 0.08, "High": 0.22}[risk_category]
        loan_status = random.choices(
            ["Active", "Closed", "Defaulted", "Written-Off"],
            weights=[0.55, 0.3, default_prob, default_prob * 0.4]
        )[0]
    elif status == "Rejected":
        rejection_reason = random.choice(REJECTION_REASONS)

    applications.append({
        "application_id": app_id,
        "customer_id": customer["customer_id"],
        "branch_id": branch["branch_id"],
        "product_id": product["product_id"],
        "application_date": app_date,
        "loan_amount_requested": requested,
        "loan_amount_approved": approved_amount,
        "tenure_months": tenure,
        "interest_rate": interest_rate,
        "emi_amount": emi,
        "application_status": status,
        "rejection_reason": rejection_reason,
        "risk_category": risk_category,
        "disbursal_date": disbursal_date,
        "loan_status": loan_status,
    })
    app_id += 1

applications_df = pd.DataFrame(applications)
applications_df.to_csv(f"{OUTPUT_DIR}/loan_applications.csv", index=False)

# ------------------------------------------------------------
# 5. Loan repayments (for approved + disbursed loans)
# ------------------------------------------------------------
repayments = []
repay_id = 1
disbursed = applications_df[applications_df["disbursal_date"].notna()]

for _, loan in disbursed.iterrows():
    n_installments_elapsed = min(
        loan["tenure_months"],
        max(1, (date.today() - pd.to_datetime(loan["disbursal_date"]).date()).days // 30)
    )
    due_date = pd.to_datetime(loan["disbursal_date"]).date() + timedelta(days=30)

    for i in range(int(n_installments_elapsed)):
        if loan["loan_status"] == "Defaulted" and i > n_installments_elapsed * 0.6:
            payment_status = "Missed"
            amount_paid = 0
            payment_date = None
            days_late = 0
        else:
            roll = random.random()
            if roll < 0.82:
                payment_status = "On-Time"
                amount_paid = loan["emi_amount"]
                payment_date = due_date
                days_late = 0
            elif roll < 0.95:
                payment_status = "Late"
                days_late = random.randint(1, 25)
                amount_paid = loan["emi_amount"]
                payment_date = due_date + timedelta(days=days_late)
            else:
                payment_status = "Missed"
                amount_paid = 0
                payment_date = None
                days_late = 0

        repayments.append({
            "repayment_id": repay_id,
            "application_id": loan["application_id"],
            "due_date": due_date,
            "emi_due": loan["emi_amount"],
            "amount_paid": amount_paid,
            "payment_date": payment_date,
            "days_late": days_late,
            "payment_status": payment_status,
        })
        repay_id += 1
        due_date = due_date + timedelta(days=30)

repayments_df = pd.DataFrame(repayments)
repayments_df.to_csv(f"{OUTPUT_DIR}/loan_repayments.csv", index=False)

print("Data generation complete:")
print(f"  branches.csv          -> {len(branches_df)} rows")
print(f"  loan_products.csv     -> {len(loan_products_df)} rows")
print(f"  customers.csv         -> {len(customers_df)} rows")
print(f"  loan_applications.csv -> {len(applications_df)} rows")
print(f"  loan_repayments.csv   -> {len(repayments_df)} rows")
