################################################################
# Difficulty: Medium
# Problem Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
################################################################


class Solution:
    def findMin(self, nums: List[int]) -> int:
        Min = self.search(nums, 0, len(nums) - 1)
        return Min

    def search(self, nums, left, right):
        mid = left + (right - left) // 2
        
        left_v, right_v, mid_v = nums[left], nums[right], nums[mid]
        if left_v <= right_v: # Sorted well, so print left_v
            return left_v
        # There are two cases remaining
        elif mid_v >= left_v: # min is between [mid_v, right_v]
            return self.search(nums, mid + 1, right)
        elif mid_v < left_v: # min is between [left_v, mid_v]
            return self.search(nums, left, mid)