################################################################
# Difficulty: Medium
# Problem Link: https://leetcode.com/problems/container-with-most-water/
################################################################


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0 , len(height) - 1
        left_h, right_h = height[left], height[right]
        maxArea = min(left_h, right_h) * (right - left)

        while left < right:
            left_h, right_h = height[left], height[right]
            area = min(left_h, right_h) * (right - left)

            if area > maxArea:
                maxArea = area
            
            if left_h >= right_h:
                right -= 1
            else:
                left += 1

        return maxArea
        