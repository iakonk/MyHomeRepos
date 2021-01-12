"""
Given a string and a list of words, find all the starting indices of substrings in the given string
that are a concatenation of all the given words exactly once without any overlapping of words.
It is given that all words are of the same length.

Example 1:

Input: String="catfoxcat", Words=["cat", "fox"]
Output: [0, 3]
Explanation: The two substring containing both the words are "catfox" & "foxcat".
"""
from collections import Counter, defaultdict


class Solution(object):
    def allConcatenations(self, string, words):
        ans = []

        w_len, w_cnt, w_freq = len(words[0]), len(words), Counter(words)
        step = w_len * w_cnt

        for i in range((len(string) - step)+1):
            seen = defaultdict(int)
            for j in range(0, w_cnt):
                next_word_index = i + j * w_len
                word = string[next_word_index: next_word_index + w_len]
                seen[word] += 1
                if word not in w_freq or seen[word] > w_freq[word]:
                    break

            if len(seen) == w_cnt and j+1 == w_cnt:
                ans.append(i)
        return ans


ans = Solution().allConcatenations("catfoxcat", ["cat", "fox"])
assert ans == [0, 3]