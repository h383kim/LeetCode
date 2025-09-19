################################################################
# Difficulty: Easy
# Problem Link: https://leetcode.com/problems/students-and-examinations/
################################################################



# Write your MySQL query statement below
SELECT temp.student_id, temp.student_name, temp.subject_name, 
    SUM(
        CASE 
        WHEN (temp.student_id = e.student_id AND 
              temp.subject_name = e.subject_name) THEN 1
        ELSE 0
        END
    ) AS attended_exams
FROM (
    SELECT * 
    FROM Students s, Subjects s2
    ) AS temp
CROSS JOIN Examinations e
GROUP BY temp.student_id, temp.student_name, temp.subject_name
ORDER BY temp.student_id, temp.subject_name
