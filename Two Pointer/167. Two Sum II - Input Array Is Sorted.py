################################################################
# Difficulty: Medium
# Problem Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
################################################################



class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            Sum = numbers[l] + numbers[r]
            if Sum == target:
                return [l + 1, r + 1]
            elif Sum < target:
                l += 1
            else:
                r -= 1