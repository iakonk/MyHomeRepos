"""
Given two binary strings (strings containing only 1s and 0s) return their sum (also as a binary string).
Note: neither binary string will contain leading 0s unless the string itself is 0

Ex: Given the following binary strings...

"100" + "1", return "101"
"11" + "1", return "100"
"1" + "0", return  "1"
"""


class Solution(object):
    def bin_sum(self, a, b):
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        res = []

        while i >= 0 or j >= 0:
            sum = carry
            if i >= 0:
                sum += int(a[i])
            if j >= 0:
                sum += int(b[j])
            res.append(sum % 2)
            carry = int(sum / 2)
            i -= 1
            j -= 1

        if carry:
            res.append(carry)

        return ''.join([str(num) for num in res[::-1]])


assert Solution().bin_sum('11', '1') == '100'
