################################################################
# Difficulty: Medium
# Problem Link: https://leetcode.com/problems/search-in-rotated-sorted-array/
################################################################



class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        # Find Pivot First(i.e. smallest)
        while l < r:
            m = l + (r - l) // 2
            if nums[r] < nums[m]:
                l = m + 1
            else:
                r = m

        pivot = l

    
        # Now Decide where the target is between two segments
        l, r = 0, len(nums) - 1
        if nums[pivot] <= target and target <= nums[r]:
            l = pivot
        else:
            r = pivot - 1

        # Now binary search on the found segment
        while l <= r:
            m = l + (r - l) // 2
            if target == nums[m]:
                return m
            elif target > nums[m]:
                l = m + 1
            else:
                r = m - 1

        return -1