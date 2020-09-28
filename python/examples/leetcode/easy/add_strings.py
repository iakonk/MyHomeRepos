class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = []
        overflow = 0

        max_len = max(len(num1), len(num2))
        for ind in range(1, max_len + 1):
            try:
                d1 = int(num1[-ind])
            except IndexError:
                d1 = 0
            try:
                d2 = int(num2[-ind])
            except IndexError:
                d2 = 0

            _sum = d1 + d2 + overflow
            overflow, _sum = divmod(_sum, 10)
            result.append(_sum)
        if overflow > 0:
            result.append(overflow)
        return ''.join([str(dig) for dig in result[::-1]])


assert Solution().addStrings('198', '188') == '386'
assert Solution().addStrings('98', '188') == '286'
assert Solution().addStrings('1', '9') == '10'
