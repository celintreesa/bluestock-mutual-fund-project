V-- 1. Top 5 Funds by Expense Ratio
SELECT scheme_name, expense_ratio_pct
FROM fact_performance
ORDER BY expense_ratio_pct DESC
LIMIT 5;

-- 2. Funds with Expense Ratio < 1%
SELECT *
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 3. Top 10 Transactions by Amount
SELECT investor_id, amount_inr
FROM fact_transactions
ORDER BY amount_inr DESC
LIMIT 10;

-- 4. Count of SIP Transactions
SELECT COUNT(*)
FROM fact_transactions
WHERE transaction_type = 'SIP';

-- 5. Count of Lumpsum Transactions
SELECT COUNT(*)
FROM fact_transactions
WHERE transaction_type = 'LUMPSUM';

-- 6. Count of Redemption Transactions
SELECT COUNT(*)
FROM fact_transactions
WHERE transaction_type = 'REDEMPTION';

-- 7. Average 1-Year Return
SELECT AVG(return_1yr_pct)
FROM fact_performance;

-- 8. Average 3-Year Return
SELECT AVG(return_3yr_pct)
FROM fact_performance;

-- 9. Average 5-Year Return
SELECT AVG(return_5yr_pct)
FROM fact_performance;

-- 10. Highest 1-Year Return Fund
SELECT scheme_name, return_1yr_pct
FROM fact_performance
ORDER BY return_1yr_pct DESC
LIMIT 1;