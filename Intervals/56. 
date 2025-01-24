################################################################
# Difficulty: Medium
# Problem Link: https://leetcode.com/problems/merge-intervals/
################################################################

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda item: (item[0], item[1]))

        result = []
        streak_start = sorted_intervals[0][0]
        streak_end = sorted_intervals[0][1]

        print(sorted_intervals)
        for interval in sorted_intervals[1:]:
            cur_start, cur_end = interval
            if streak_end >= cur_start:
                streak_end = max(streak_end, cur_end)
            else:
                result.append([streak_start, streak_end])
                streak_start = cur_start
                streak_end = cur_end

        if len(result) == 0:
            result.append([streak_start, streak_end])
            return result

        if cur_start != result[-1][0]:
            result.append([streak_start, streak_end])

        return result