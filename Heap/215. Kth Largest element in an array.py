################################################################
# Difficulty: Medium
# Problem Link: https://leetcode.com/problems/kth-largest-element-in-an-array/
################################################################


import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap = []

        heapq.heapify(heap)
        for num in nums:
            heapq.heappush(heap, -num)

        for i in range(k):
            result = heapq.heappop(heap)

        return -result