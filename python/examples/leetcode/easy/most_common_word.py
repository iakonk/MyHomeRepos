class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        import collections

        for c in ['?', ':', '!', ';', '.', ',']:
            paragraph = paragraph.replace(c, ' ')
        aggr = collections.Counter(paragraph.lower().split())

        banned_set = set(banned)
        ans, max_cnt = None, 0
        for word, cnt in aggr.items():
            if word not in banned_set and cnt > max_cnt:
                ans, max_cnt = word, cnt
        return ans


print(Solution().mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"]))