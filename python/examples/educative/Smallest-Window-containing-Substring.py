"""
Given a string and a pattern, find the smallest substring in the given string which has all the characters of the
given pattern.

Example 1:

Input: String="aabdec", Pattern="abc"
Output: "abdec"
Explanation: The smallest substring having all characters of the pattern is "abdec"
"""
from collections import Counter


class Solution(object):

    def findSmallestSubstring(self, string, pattern):
        start = min_s_start = match = 0
        min_len = float('inf')
        aggr = Counter(pattern)

        for end, c in enumerate(string):
            if c in aggr:
                aggr[c] -= 1
                match += aggr[c] >= 0

            while match == len(pattern):
                if min_len > end - start + 1:
                    min_len = end - start + 1
                    min_s_start = start

                lc = string[start]
                start += 1
                if lc in aggr:
                    match -= aggr[lc] == 0
                    aggr[lc] += 1

        if min_len > len(string):
            return ""
        return string[min_s_start:min_s_start+min_len]


ans = Solution().findSmallestSubstring("abdbca", "abc")
assert ans == 'bca', ans

ans = Solution().findSmallestSubstring('aabdec', 'abc')
assert ans == 'abdec'


ans = Solution().findSmallestSubstring('adcad', 'abc')
assert ans == ''

