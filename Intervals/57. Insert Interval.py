################################################################
# Difficulty: Medium
# Problem Link: https://leetcode.com/problems/insert-interval/
################################################################



class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if len(intervals) == 0:
            return [newInterval]

        newInterval_s, newInterval_e = newInterval

        result = []

        streak_s, streak_e = newInterval
        body_added = False

        for idx, cur_interval in enumerate(intervals):
            cur_interval_s, cur_interval_e = cur_interval
            
            # Head
            if newInterval_s > cur_interval_e:
                result.append(cur_interval)
                continue
            
            # Tail
            if newInterval_e < cur_interval_s:
                if not body_added:
                    result.append([streak_s, streak_e])
                    body_added = True

                result.append(cur_interval)
                continue

            # Body
            streak_s = min(cur_interval_s, streak_s)
            streak_e = max(cur_interval_e, streak_e)

        if not body_added:
            result.append([streak_s, streak_e])
        
        return result
            
