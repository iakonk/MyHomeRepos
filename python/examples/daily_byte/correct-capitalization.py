"""
Given a string, return whether or not it uses capitalization correctly.
A string correctly uses capitalization if all letters are capitalized,
no letters are capitalized, or only the first letter is capitalized.

Ex: Given the following strings...
"USA", return true
"Calvin", return true
"compUter", return false
"coding", return true
"""


class Solution(object):
    def is_valid_capitalization(self, chars):
        cc = 0
        for c in chars:
            cc += c.isupper()

        if cc == 1 and chars[0].isupper():
            return True
        elif cc == len(chars) or not cc:
            return True
        else:
            return False


assert Solution().is_valid_capitalization("USA")
assert Solution().is_valid_capitalization("Calvin")
assert Solution().is_valid_capitalization("coding")

assert not Solution().is_valid_capitalization("compUter")