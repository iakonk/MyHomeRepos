"""
String Anagrams (hard) #
Given a string and a pattern, find all anagrams of the pattern in the given string.

Anagram is actually a Permutation of a string. For example, “abc” has the following six anagrams:

abc
acb
bac
bca
cab
cba
Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

Example 1:

Input: String="ppqp", Pattern="pq"
Output: [1, 2]
Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".
"""
from collections import Counter


class Solution(object):
    def findAllAnagrams(self, string, ptrn):
        aggr = Counter(ptrn)
        start = matches = 0
        ans = []
        for end, c in enumerate(string):
            if c in aggr:
                aggr[c] -= 1
                matches += aggr[c] == 0

            if matches == len(ptrn):
                ans.append(start)

            if end >= len(ptrn) - 1:
                lc = string[start]
                start += 1
                if lc in aggr:
                    matches -= aggr[lc] == 0
                    aggr[lc] += 1
        return ans


ans = Solution().findAllAnagrams('ppqp', 'pq')
print(ans)