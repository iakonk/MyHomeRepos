class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min_price = prices[0]
        # [7,1,5,3,6,4]
        for ind in range(0, len(prices)):
            if prices[ind] <= min_price:
                min_price = prices[ind]
            else:
                max_profit = max(max_profit, prices[ind] - min_price)
        return max_profit


assert Solution().maxProfit([7,1,5,3,6,4]) == 5
assert Solution().maxProfit([7,6,4,3,1]) == 0