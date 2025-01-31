"""
https://leetcode.com/problems/fizz-buzz/
"""


class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        next_m1, next_m2, next_m3 = 3, 5, 15
        ans = [0] * (n+1)
        for ind in range(1, n+1):
            if ind == next_m3:
                ans[ind] = 'FizzBuzz'
                next_m3 += 15
                next_m1 += 3
                next_m2 += 5

            elif ind == next_m1:
                ans[ind] = 'Fizz'
                next_m1 += 3
            elif ind == next_m2:
                ans[ind] = 'Buzz'
                next_m2 += 5
            else:
                ans[ind] = str(ind)
        return ans[1:]

