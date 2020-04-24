class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        orig, x = x, abs(x)
        reversed_num = 0
        while x != 0:
            x, last_digit = x // 10, x % 10
            reversed_num = reversed_num * 10 + last_digit
            if not -2 ** 31 <= reversed_num <= 2 ** 31 - 1:
                return 0
        return reversed_num if orig > 0 else -reversed_num

assert Solution().reverse(0) == 0
assert Solution().reverse(10) == 1, Solution().reverse(10)
assert Solution().reverse(-123) == -321, Solution().reverse(-123)

# corner cases:
# [0, 9]
#  < 0
# [−231,  231 − 1]