################################################################
# Difficulty: Easy
# Problem Link: https://leetcode.com/problems/last-stone-weight/
################################################################


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            max1 = heapq.heappop(stones) # -largest
            max2 = heapq.heappop(stones) # -second_largest
            if max2 > max1:
                heapq.heappush(stones, max1 - max2)

        if len(stones) == 0:
            return 0
            
        return abs(stones[0])