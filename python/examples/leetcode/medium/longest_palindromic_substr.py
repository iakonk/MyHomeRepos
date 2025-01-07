class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        max_s_len = 0
        for i in range(len(s)):
            tmp = expand(s, i, i)
            max_s_len = max(tmp, max_s_len)
            tmp = expand(s, i, i + 1)
            max_s_len = max(max_s_len, tmp)
        return max_s_len


