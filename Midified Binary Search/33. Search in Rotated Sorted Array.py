################################################################
# Difficulty: Medium
# Problem Link: https://leetcode.com/problems/search-in-rotated-sorted-array/
################################################################


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1

        def binSearch(l, r):
            while l <= r:
                m = l + (r - l) // 2
                m_val = nums[m]

                if m_val == target:
                    return m
                elif m_val > target:
                    if nums[l] < nums[r]:
                        return binSearch(l, m - 1)
                    elif nums[l] <= nums[m]: # l < target < m or target < l < m
                        if nums[l] > target:
                            return binSearch(m + 1, r)
                        else:
                            return binSearch(l, m - 1)
                    else:   # target < m < l
                        return binSearch(l, m - 1)
                else: # m_val < target
                    if nums[l] < nums[r]:
                        return binSearch(m + 1, r)
                    elif nums[l] < nums[m]: # l < m < target
                        return binSearch(m + 1, r)
                    else: # l > target > m or target > l > m
                        if nums[l] > target:
                            return binSearch(m + 1, r)
                        else:
                            return binSearch(l, m - 1)
            return -1

        return binSearch(l, r)