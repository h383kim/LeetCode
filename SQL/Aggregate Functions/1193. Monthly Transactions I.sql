################################################################
# Difficulty: Medium
# Problem Link: https://leetcode.com/problems/monthly-transactions-i/
################################################################


# Write your MySQL query statement below
SELECT 
    DATE_FORMAT(trans_date, "%Y-%m") as month, 
    country, 
    COUNT(*) as trans_count,
    SUM(IF(state='approved', 1, 0)) as approved_count,
    SUM(amount) as trans_total_amount,
    SUM(IF(state='approved', amount, 0)) as approved_total_amount
FROM Transactions
GROUP BY country, DATE_FORMAT(trans_date, "%Y-%m")