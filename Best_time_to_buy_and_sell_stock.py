'''
Leed Code question no: 121
Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit =0
        minCost = prices[0]
        for i in range(1,len(prices)):
            if ((prices[i]- minCost)>profit):
                profit = prices[i]-minCost
            if(prices[i] < minCost):
                minCost = prices[i]
                
        return profit