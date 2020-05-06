# https://www.youtube.com/watch?v=jgiZlGzXMBw
# You are given coins of different denominations and a total amount of money amount.
# Write a function to compute the fewest number of coins that you need to make up that amount.
# If that amount of money cannot be made up by any combination of the coins, return -1.
# Example 1:
# Input: coins = [1, 2, 5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:
#
# Input: coins = [2], amount = 3
# Output: -1


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        res = [amount + 1] * (amount + 1)
        res[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    res[i] = min(res[i], res[i-coin] + 1)

        ans = res[amount]
        return ans if ans != amount + 1 else -1


ans = Solution().coinChange([1, 2, 5], 11)
assert ans == 3


ans = Solution().coinChange([2], 3)
assert ans == -1

