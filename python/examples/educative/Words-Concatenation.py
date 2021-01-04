"""
Given a string and a list of words, find all the starting indices of substrings in the given string
that are a concatenation of all the given words exactly once without any overlapping of words.
It is given that all words are of the same length.

Example 1:

Input: String="catfoxcat", Words=["cat", "fox"]
Output: [0, 3]
Explanation: The two substring containing both the words are "catfox" & "foxcat".
"""
from collections import Counter


class Solution(object):
    def allConcatenations(self, string, words):
        words = set(words)
        start = match = 0
        step = len(words[0]) * len(words)
        ans = []

        for i in range(0, len(string), step):
            end = min(i+step, len(string))
            one_w = string[i:end]

            if one_w in words:
                if aggr[one_w] == 0:
                    
                else:
                    aggr[one_w] -= 1
                match += aggr[one_w] >= 0




            while match == len(words):
                ans.append(start)
                lw = words[start]
                start += 1
                match -= aggr[lw] == 0
                aggr[lw] += 1
