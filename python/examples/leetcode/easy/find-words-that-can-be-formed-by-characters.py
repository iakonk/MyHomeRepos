class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        import collections

        result = 0
        chars_cnt = collections.Counter(chars)

        for w in words:
            word_c_cnt = collections.Counter(w)
            matched = sum((word_c_cnt & chars_cnt).values())
            if matched == sum(word_c_cnt.values()):
                result += matched
        return result


ans = Solution().countCharacters(["cat","bt","hat","tree"], "atach")
assert ans == 6