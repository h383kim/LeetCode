################################################################
# Difficulty: Easy
# Problem Link: https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/
################################################################



# Write your MySQL query statement below
WITH temp AS (
    SELECT t.transaction_id, t.visit_id, v.customer_id
    FROM Visits v
    LEFT OUTER JOIN Transactions t
    ON t.visit_id = v.visit_id
)
SELECT customer_id, COUNT(*) AS count_no_trans
FROM temp
WHERE transaction_id IS NULL
GROUP BY customer_id