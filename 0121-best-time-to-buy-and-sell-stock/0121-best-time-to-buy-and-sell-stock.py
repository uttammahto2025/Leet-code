class Solution:
    def maxProfit(self, prices):
        TEMP= prices[0]
        profit = 0
        for price in prices:
            TEMP= min(TEMP, price)
            profit = max(profit, price -TEMP)
        return profit