-- ============================================================
-- Bank Loan & Credit Risk Analytics (India)
-- Database Schema
-- ============================================================
-- Engine target: MySQL 8.0+ / PostgreSQL 13+ compatible
-- Author: Malleshwari C
-- ============================================================

DROP TABLE IF EXISTS loan_repayments;
DROP TABLE IF EXISTS loan_applications;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS branches;
DROP TABLE IF EXISTS loan_products;

-- ------------------------------------------------------------
-- 1. Branches: bank branch network across India
-- ------------------------------------------------------------
CREATE TABLE branches (
    branch_id        INT PRIMARY KEY AUTO_INCREMENT,
    branch_name      VARCHAR(100) NOT NULL,
    city             VARCHAR(50)  NOT NULL,
    state            VARCHAR(50)  NOT NULL,
    zone             VARCHAR(20)  NOT NULL,        -- North / South / East / West / Central
    branch_type      VARCHAR(20)  NOT NULL,        -- Urban / Semi-Urban / Rural / Metro
    opened_date      DATE         NOT NULL
);

-- ------------------------------------------------------------
-- 2. Loan products: types of loans offered
-- ------------------------------------------------------------
CREATE TABLE loan_products (
    product_id       INT PRIMARY KEY AUTO_INCREMENT,
    product_name     VARCHAR(50)  NOT NULL,        -- Home, Personal, Auto, Education, Gold, Business
    interest_type    VARCHAR(20)  NOT NULL,        -- Fixed / Floating
    min_interest_rate DECIMAL(5,2) NOT NULL,
    max_interest_rate DECIMAL(5,2) NOT NULL,
    min_tenure_months INT NOT NULL,
    max_tenure_months INT NOT NULL,
    processing_fee_pct DECIMAL(4,2) NOT NULL
);

-- ------------------------------------------------------------
-- 3. Customers
-- ------------------------------------------------------------
CREATE TABLE customers (
    customer_id      INT PRIMARY KEY AUTO_INCREMENT,
    full_name        VARCHAR(100) NOT NULL,
    gender           VARCHAR(10)  NOT NULL,
    date_of_birth    DATE         NOT NULL,
    city             VARCHAR(50)  NOT NULL,
    state            VARCHAR(50)  NOT NULL,
    occupation_type  VARCHAR(30)  NOT NULL,        -- Salaried / Self-Employed / Business Owner / Retired
    annual_income    DECIMAL(12,2) NOT NULL,
    credit_score     INT NOT NULL,                  -- CIBIL-style score 300-900
    existing_emi_monthly DECIMAL(10,2) DEFAULT 0,
    bank_relationship_years DECIMAL(4,1) NOT NULL,
    signup_date      DATE NOT NULL
);

-- ------------------------------------------------------------
-- 4. Loan applications: core fact table
-- ------------------------------------------------------------
CREATE TABLE loan_applications (
    application_id     INT PRIMARY KEY AUTO_INCREMENT,
    customer_id        INT NOT NULL,
    branch_id           INT NOT NULL,
    product_id          INT NOT NULL,
    application_date    DATE NOT NULL,
    loan_amount_requested DECIMAL(12,2) NOT NULL,
    loan_amount_approved  DECIMAL(12,2),
    tenure_months        INT NOT NULL,
    interest_rate         DECIMAL(5,2),
    emi_amount             DECIMAL(10,2),
    application_status     VARCHAR(20) NOT NULL,    -- Approved / Rejected / Pending / Withdrawn
    rejection_reason       VARCHAR(100),
    risk_category           VARCHAR(10),            -- Low / Medium / High
    disbursal_date           DATE,
    loan_status               VARCHAR(20),          -- Active / Closed / Defaulted / Written-Off / NA
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (branch_id) REFERENCES branches(branch_id),
    FOREIGN KEY (product_id) REFERENCES loan_products(product_id)
);

-- ------------------------------------------------------------
-- 5. Loan repayments: monthly repayment tracking
-- ------------------------------------------------------------
CREATE TABLE loan_repayments (
    repayment_id      INT PRIMARY KEY AUTO_INCREMENT,
    application_id     INT NOT NULL,
    due_date            DATE NOT NULL,
    emi_due             DECIMAL(10,2) NOT NULL,
    amount_paid          DECIMAL(10,2) NOT NULL,
    payment_date          DATE,
    days_late              INT DEFAULT 0,
    payment_status          VARCHAR(20) NOT NULL,   -- On-Time / Late / Missed
    FOREIGN KEY (application_id) REFERENCES loan_applications(application_id)
);

-- ------------------------------------------------------------
-- Indexes for query performance
-- ------------------------------------------------------------
CREATE INDEX idx_app_customer ON loan_applications(customer_id);
CREATE INDEX idx_app_branch ON loan_applications(branch_id);
CREATE INDEX idx_app_product ON loan_applications(product_id);
CREATE INDEX idx_app_status ON loan_applications(application_status);
CREATE INDEX idx_app_date ON loan_applications(application_date);
CREATE INDEX idx_repay_app ON loan_repayments(application_id);
CREATE INDEX idx_repay_status ON loan_repayments(payment_status);
CREATE INDEX idx_cust_score ON customers(credit_score);
