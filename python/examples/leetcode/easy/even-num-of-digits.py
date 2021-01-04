"""
Input: nums = [12,345,2,6,7896]
Output: 2
Explanation:
12 contains 2 digits (even number of digits).
345 contains 3 digits (odd number of digits).
2 contains 1 digit (odd number of digits).
6 contains 1 digit (odd number of digits).
7896 contains 4 digits (even number of digits).
Therefore only 12 and 7896 contain an even number of digits.

"""

class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def r(n):
            if not n: return 0
            return 1 + r(n // 10)

        c = 0
        for n in nums:
            c += r(n) % 2 == 0
        return c


ans = Solution().findNumbers([12,345,2,6,7896])
assert ans == 2
