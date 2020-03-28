class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        s = ''.join(re.findall(r'\w+', s))
        left_ind, right_ind = 0, len(s) - 1

        while left_ind < right_ind:
            if s[left_ind].lower() != s[right_ind].lower():
                return False
            left_ind += 1
            right_ind -= 1
        return True


assert Solution().isPalindrome("0P") == False
assert Solution().isPalindrome("A man, a plan, a canal: Panama")
assert Solution().isPalindrome(" ara")
