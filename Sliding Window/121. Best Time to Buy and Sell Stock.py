################################################################
# Difficulty: Easy
# Problem Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
################################################################



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        MaxProfit = 0
        buy, sell = prices[0], 0

        for p in prices[1:]:
            
            if buy > p:
                buy = p
                sell = 0
                continue 
            if sell < p and p > buy:
                sell = p
                MaxProfit = max(MaxProfit, sell - buy)

        return MaxProfit