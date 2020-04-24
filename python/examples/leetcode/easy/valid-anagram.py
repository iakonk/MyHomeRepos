class Solution(object):
    """
    Runtime: 76 ms, faster than 9.71% of Python online submissions for Valid Anagram.
    Memory Usage: 12.9 MB, less than 55.26% of Python online submissions for Valid Anagram.
    """
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        import collections

        aggr = collections.Counter(t)
        for char in s:
            if char not in aggr:
                return False
            if char in aggr:
                aggr[char] -= 1
                if aggr[char] <= 0:
                    del aggr[char]
        return len(aggr) == 0


ans = Solution().isAnagram('ab', 'a')
print(ans)


class Solution(object):
    """
    Runtime: 40 ms, faster than 70.84% of Python online submissions for Valid Anagram.
    Memory Usage: 13.5 MB, less than 15.79% of Python online submissions for Valid Anagram.
    """
    def isAnagram(self, s, t):
        """"""
        return sorted(s) == sorted(t)


ans = Solution().isAnagram('', 'a')
print(ans)
