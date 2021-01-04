"""
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
"""


class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo, hi = 0, n
        while lo <= hi:
            k=(lo+hi)//2
            curr = k*(k+1)//2
            if curr == n:
                return k
            elif curr > n:
                hi = k - 1
            else:
                lo = k + 1
        return hi


ans = Solution().arrangeCoins(5)
print(ans)
