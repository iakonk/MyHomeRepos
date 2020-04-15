# Runtime: 48 ms, faster than 31.54% of Python online submissions for Reverse Words in a String III.
# Memory Usage: 13.9 MB, less than 9.09% of Python online submissions for Reverse Words in a String III.


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join([w[::-1] for w in s.split()])
        # words = s.split()
        # seen = {}
        # for ind, w in enumerate(words):
        #     if w not in seen:
        #         r = ''.join([char for char in reversed(w)])
        #         seen[w] = r
        #     words[ind] = seen[w]
        # return ' '.join(words)


# ans = Solution().reverseWords("Let's take LeetCode contest")
ans = Solution().reverseWords("s'a a's s'x")
print(ans)
