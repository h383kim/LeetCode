################################################################
# Difficulty: Medium
# Problem Link: https://leetcode.com/problems/subarray-sum-equals-k/
################################################################



class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_freq = {0: 1}

        cumSum = 0
        count = 0
        for num in nums:
            cumSum += num
            diff = cumSum - k
            
            if diff in sum_freq:
                count += sum_freq[diff]

            sum_freq[cumSum] = sum_freq.get(cumSum, 0) + 1

        return count