################################################################
# Difficulty: Medium
# Problem Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        total = 0
        for i in range(1, len(prices)):
            if prices[i] > buy:
                total += prices[i] - buy
                buy = prices[i]
            elif prices[i] < buy:
                buy = prices[i]
        
        return total