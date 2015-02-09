class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        maxProfit = 0
        minPrice = 2 ** 31 - 1
        for i in prices:
            minPrice = min(minPrice, i)
            maxProfit = max(maxProfit, i - minPrice)
        return maxProfit