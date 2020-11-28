"""
Given a string, reverse all of its characters and return the resulting string.

Ex: Given the following strings...

“Cat”, return “taC”
“The Daily Byte”, return "etyB yliaD ehT”
“civic”, return “civic”
"""


class Solution(object):
    def reverse_string(self, string_):
        return ''.join([ch for ch in string_[::-1]])


assert Solution().reverse_string('The Daily Byte') == 'etyB yliaD ehT'


# This question is asked by Facebook. Given a string, return whether or not it forms a
# palindrome ignoring case and non-alphabetical characters.
# Note: a palindrome is a sequence of characters that reads the same forwards and backwards.
#
# Ex: Given the following strings...
#
# "level", return true
# "algorithm", return false
# "A man, a plan, a canal: Panama.", return true


class Solution(object):
    def is_palindrome(self, str):

        left, right = 0, len(str) - 1
        while left < right:
            if not str[left].isalpha():
                left += 1
            elif not str[right].isalpha():
                right -= 1
            else:
                if str[left].lower() != str[right].lower():
                    return False
                else:
                    left += 1
                    right -= 1
        return True


assert Solution().is_palindrome('A man, a plan, a canal: Panama.')
assert Solution().is_palindrome('level')
assert not Solution().is_palindrome('algorithm')
