################################################################
# Difficulty: Easy
# Problem Link: https://leetcode.com/problems/binary-search/
################################################################



class Solution:
    def search(self, nums: List[int], target: int) -> int:

        mid = len(nums) // 2

        if len(nums) == 0:
            return -1

        while len(nums) > 0:
            if nums[mid] < target:
                right_search = self.search(nums[mid + 1:], target)
                return right_search + (mid + 1) if right_search != -1 else -1 # Adjust index if found
            elif nums[mid] > target:
                return self.search(nums[:mid], target) # Search in left half
            elif nums[mid] == target:
                return mid  # Return mid if target is found