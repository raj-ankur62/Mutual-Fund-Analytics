--  Analytical SQL Queries
-- 1. Top 5 Funds by AUM
SELECT fund_name, aum_crore
FROM scheme_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV per Month
SELECT
    strftime('%Y-%m', date) AS month,
    ROUND(AVG(nav), 2) AS avg_nav
FROM nav_history
GROUP BY month
ORDER BY month;

-- 3. SIP Year-over-Year Growth
SELECT
    strftime('%Y', transaction_date) AS year,
    COUNT(*) AS sip_transactions,
    SUM(amount_inr) AS total_sip_amount
FROM investor_transactions
WHERE transaction_type = 'SIP'
GROUP BY year
ORDER BY year;

-- 4. Transactions by State
SELECT
    state,
    COUNT(*) AS total_transactions
FROM investor_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- 5. Funds with Expense Ratio less than 1%
SELECT
    scheme_name,
    expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;

-- 6. Top 5 Funds by Sharpe Ratio
SELECT
    scheme_name,
    sharpe_ratio
FROM scheme_performance
ORDER BY sharpe_ratio DESC
LIMIT 5;

-- 7. Average Expense Ratio by Risk Grade
SELECT
    risk_grade,
    ROUND(AVG(expense_ratio_pct),2) AS avg_expense_ratio
FROM scheme_performance
GROUP BY risk_grade;

-- 8. Average Transaction Amount by Payment Mode
SELECT
    payment_mode,
    ROUND(AVG(amount_inr),2) AS avg_amount
FROM investor_transactions
GROUP BY payment_mode
ORDER BY avg_amount DESC;

-- 9. Number of Investors by KYC Status
SELECT
    kyc_status,
    COUNT(*) AS investor_count
FROM investor_transactions
GROUP BY kyc_status;

-- 10. Top 5 Funds by Benchmark Return
SELECT
    scheme_name,
    benchmark_3yr_pct
FROM scheme_performance
ORDER BY benchmark_3yr_pct DESC
LIMIT 5;