################################################################
# Difficulty: Easy
# Problem Link: https://leetcode.com/problems/project-employees-i/
################################################################


# Write your MySQL query statement below
SELECT p.project_id, ROUND(AVG(e.experience_years), 2) AS average_years
FROM Employee e, Project p
WHERE e.employee_id = p.employee_id
GROUP BY p.project_id