# https://leetcode.com/problems/top-k-frequent-words/
# Given a non-empty list of words, return the k most frequent elements.
#
# Your answer should be sorted by frequency from highest to lowest.
# If two words have the same frequency, then the word with the lower alphabetical order comes first.
import heapq
import collections


class HeapObj:
    def __init__(self, word, cnt):
        self.word = word
        self.cnt = cnt

    def __lt__(self, other):
        return (self.cnt < other.cnt) or (self.cnt == other.cnt and self.word > other.word)


class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        aggr = collections.Counter(words)
        h = []
        for w, cnt in aggr.items():
            obj = HeapObj(w, cnt)
            heapq.heappush(h, obj)
            if len(h) > k:
                heapq.heappop(h)
        print([(w.word, w.cnt) for w in h])
        return [obj.word for obj in sorted(h, reverse=True)]


assert Solution().topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2) == ["i", "love"]
assert Solution().topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4) == ["the","is","sunny","day"]
assert Solution().topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 3) == ["i","love","coding"]
