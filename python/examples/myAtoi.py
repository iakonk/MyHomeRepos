import re


# Implement atoi which converts a string to an integer.
#
# The function first discards as many whitespace characters as necessary until the first non-whitespace
# character is found. Then, starting from this character, takes an optional initial plus or minus sign
# followed by as many numerical digits as possible, and interprets them as a numerical value.
#
# The string can contain additional characters after those that form the integral number,
# which are ignored and have no effect on the behavior of this function.
#
# If the first sequence of non-whitespace characters in str is not a valid integral number,
# or if no such sequence exists because either str is empty or it contains only whitespace characters,
# no conversion is performed.
#
# If no valid conversion could be performed, a zero value is returned.
#
# Note:
# Only the space character ' ' is considered as whitespace character.
# Assume we are dealing with an environment which could only store integers within the 32-bit signed
# integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values,
# INT_MAX (231 − 1) or INT_MIN (−231) is returned.

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        default_return_val = 0
        int_min = -2 ** 31      # 2147483647
        int_max = 2 ** 31 - 1   # -2147483648

        if not str:
            return default_return_val

        number = re.search("[-+]?\d{1,}", str)
        if not number:
            return default_return_val

        num_start_pos = number.start()
        for char in str[:num_start_pos]:
            if char != ' ':
                return default_return_val

        int_ = int(number.group(0))
        if int_min <= int_ <= int_max:
            return int_
        if int_ > 0:
            return int_max
        else:
            return int_min


assert Solution().myAtoi("words and 987") == 0
assert Solution().myAtoi("42") == 42
assert Solution().myAtoi("   -42") == -42
assert Solution().myAtoi("4193 with words") == 4193
assert Solution().myAtoi("-91283472332") == -2147483648, Solution().myAtoi("-91283472332")
assert Solution().myAtoi("2147483647") == 2147483647, Solution().myAtoi("2147483647")
assert Solution().myAtoi("2147483648") == 2147483647, Solution().myAtoi("2147483648")
