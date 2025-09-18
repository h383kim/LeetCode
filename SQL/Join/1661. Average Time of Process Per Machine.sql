################################################################
# Difficulty: Easy
# Problem Link: https://leetcode.com/problems/average-time-of-process-per-machine/
################################################################



# Write your MySQL query statement below
SELECT machine_id, ROUND(SUM(temp.diff) / COUNT(*), 3) AS processing_time
FROM (
    SELECT a1.machine_id, a1.process_id, 
           (a2.timestamp - a1.timestamp) AS diff
    FROM Activity a1, Activity a2
    WHERE a1.process_id = a2.process_id
    AND a1.machine_id = a2.machine_id
    AND a1.activity_type = 'start'
    AND a2.activity_type = 'end'
) AS temp
GROUP BY temp.machine_id