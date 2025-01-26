################################################################
# Difficulty: Medium
# Problem Link: https://leetcode.com/problems/top-k-frequent-elements/
################################################################


import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Create the num : frequency hash map
        freq_dict = {}
        for num in nums:
            freq_dict[num] = freq_dict.get(num, 0) + 1
        
        # Creat min-heap based on frequency as priority  
        heap = []
        for key, val in freq_dict.items():
            # Simply push until the heap contains k elements
            if len(heap) < k:
                heapq.heappush(heap, (val, key))
            # If more than k elements are in the heap
            else:
                heapq.heappush(heap, (val, key)) # Push the new element
                heapq.heappop(heap) # Pop the min-frequent item

        res = []
        for (val, key) in heap:
            res.append(key)
        
        return res