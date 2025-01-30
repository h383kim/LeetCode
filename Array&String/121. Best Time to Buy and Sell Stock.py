################################################################
# Difficulty: Easy
# Problem Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
################################################################

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        buy = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > buy:
                maxProfit = max(maxProfit, prices[i] - buy)
            elif prices[i] < buy:
                buy = prices[i]
        
        return maxProfit