################################################################
# Difficulty: Medium
# Problem Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
################################################################


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        for i in range(len(numbers)):
            l, r = i + 1, len(numbers) - 1
            diff = target - numbers[i]
            while l <= r:
                m = l + (r - l) // 2
                m_val = numbers[m]
                if m_val == diff:
                    return [i + 1, m + 1]
                elif m_val < diff:
                    l = m + 1
                else:
                    r = m - 1