class Solution(object):
    def longestPalindrome(self, s):
        """
        Brute force
        :type s: str
        :rtype: str
        """
        def is_pal(subst):
            left = 0
            right = len(subst) - 1
            while left < right:
                if subst[left] != subst[right]:
                    return False
                left += 1
                right -= 1
            return True

        max_len = 0
        pal = ""
        for i in range(len(s)):
            j = i +1
            while j < len(s):
                if is_pal(s[i:j]) and j-i > max_len:
                    max_len = j-1
                    pal = s[i:j]
                j += 1
        return pal


ans = Solution().longestPalindrome("cbbd")
assert ans == 'bb'

ans = Solution().longestPalindrome("babad")
assert ans == 'aba'


class Solution(object):
    def longestPalindrome(self, s):
        """

        :type s: str
        :rtype: str
        """
        if s