################################################################
# Difficulty: Easy
# Problem Link: https://leetcode.com/problems/percentage-of-users-attended-a-contest/
################################################################


# Write your MySQL query statement below
WITH total AS (
    SELECT user_id, COUNT(DISTINCT user_id) AS cnt
    FROM Users
)
SELECT r.contest_id, ROUND(100 * COUNT(*) / t.cnt, 2) AS percentage
FROM Users u JOIN Register r
ON u.user_id = r.user_id
CROSS JOIN total t
GROUP BY r.contest_id
ORDER BY percentage DESC, r.contest_id ASC