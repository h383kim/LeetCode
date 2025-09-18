################################################################
# Difficulty: Medium
# Problem Link: https://leetcode.com/problems/managers-with-at-least-5-direct-reports/
################################################################



# Write your MySQL query statement below
SELECT e1.name
FROM Employee e1, Employee e2
WHERE e1.id = e2.managerId
GROUP BY e1.id
HAVING COUNT(*) >= 5
