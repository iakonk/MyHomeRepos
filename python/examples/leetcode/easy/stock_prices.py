# Say you have an array for which the ith element is the price of a given stock on day i.
#
# If you were only permitted to complete at most one transaction
# (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
#
# Note that you cannot sell a stock before you buy one.
#
# Example 1:
#
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min_price = prices[0]
        # [7,1,5,3,6,4]
        for price in prices:
            if price <= min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
        return max_profit


assert Solution().maxProfit([7,1,5,3,6,4]) == 5
assert Solution().maxProfit([7,6,4,3,1]) == 0