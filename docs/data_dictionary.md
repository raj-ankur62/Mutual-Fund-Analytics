# Data Dictionary

## Project: Mutual Fund Analytics

This document describes the datasets used in the Mutual Fund Analytics project, including column names, data types, business definitions, and data sources.

---

# Dataset 1: nav_history_clean.csv

**Source:** 02_nav_history.csv

| Column Name | Data Type | Business Definition |
|-------------|-----------|---------------------|
| amfi_code | Integer | Unique AMFI code identifying the mutual fund scheme |
| date | Date | NAV calculation date |
| nav | Decimal | Net Asset Value of the scheme on the given date |

---

# Dataset 2: investor_transactions_clean.csv

**Source:** 08_investor_transactions.csv

| Column Name | Data Type | Business Definition |
|-------------|-----------|---------------------|
| investor_id | String | Unique investor identifier |
| transaction_date | Date | Date of transaction |
| amfi_code | Integer | Mutual fund scheme AMFI code |
| transaction_type | String | Type of transaction (SIP, Lumpsum, Redemption) |
| amount_inr | Decimal | Transaction amount in INR |
| state | String | Investor's state |
| city | String | Investor's city |
| city_tier | String | City classification (Tier 1, Tier 2, Tier 3) |
| age_group | String | Investor age category |
| gender | String | Investor gender |
| annual_income_lakh | Decimal | Annual income (Lakhs INR) |
| payment_mode | String | Mode of payment |
| kyc_status | String | KYC verification status (Verified/Pending) |

---

# Dataset 3: scheme_performance_clean.csv

**Source:** 07_scheme_performance.csv

| Column Name | Data Type | Business Definition |
|-------------|-----------|---------------------|
| amfi_code | Integer | Unique AMFI scheme code |
| scheme_name | String | Name of mutual fund scheme |
| category | String | Fund category |
| fund_house | String | Asset Management Company |
| return_1yr_pct | Decimal | One-year return (%) |
| return_3yr_pct | Decimal | Three-year return (%) |
| return_5yr_pct | Decimal | Five-year return (%) |
| benchmark_3yr_pct | Decimal | Three-year benchmark return (%) |
| alpha | Decimal | Alpha performance metric |
| beta | Decimal | Beta risk metric |
| sharpe_ratio | Decimal | Risk-adjusted return ratio |
| sortino_ratio | Decimal | Downside risk-adjusted return ratio |
| std_dev_ann_pct | Decimal | Annualized standard deviation (%) |
| max_drawdown_pct | Decimal | Maximum historical drawdown (%) |
| aum_crore | Decimal | Assets Under Management (Crore INR) |
| expense_ratio_pct | Decimal | Expense ratio (%) |
| morningstar_rating | Integer | Morningstar fund rating |
| risk_grade | String | Fund risk category |

---

# Data Sources

| Dataset | Source |
|---------|--------|
| Fund Master | 01_fund_master.csv |
| NAV History | 02_nav_history.csv |
| AUM by Fund House | 03_aum_by_fund_house.csv |
| Monthly SIP Inflows | 04_monthly_sip_inflows.csv |
| Category Inflows | 05_category_inflows.csv |
| Industry Folio Count | 06_industry_folio_count.csv |
| Scheme Performance | 07_scheme_performance.csv |
| Investor Transactions | 08_investor_transactions.csv |
| Portfolio Holdings | 09_portfolio_holdings.csv |
| Benchmark Indices | 10_benchmark_indices.csv |

---

## Notes

- Dates are stored in YYYY-MM-DD format.
- Currency values are represented in Indian Rupees (INR).
- Percentage values are stored as numeric percentages.
- Cleaned datasets are stored in the `data/processed/` folder.