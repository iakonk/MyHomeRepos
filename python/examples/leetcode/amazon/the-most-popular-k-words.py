# https://leetcode.com/discuss/interview-question/542597/

# Given a list of reviews, a list of keywords and an integer k.
# Find the most popular k keywords in order of most to least frequently mentioned.
#
# The comparison of strings is case-insensitive.
# Multiple occurances of a keyword in a review should be considred as a single mention.
# If keywords are mentioned an equal number of times in reviews, sort alphabetically.
import heapq
import re


class HeapObj:
    def __init__(self, word, cnt):
        self.word = word
        self.cnt = cnt

    def __lt__(self, other):
        # if cnt is equal, compare strings
        # lexicographically bigger word should be on top
        return (self.cnt < other.cnt) or ((self.cnt == other.cnt) and (self.word > other.word))

    def __str__(self):
        return str(self.word)


def top_freq_words(k, keywords, reviews):
    aggr = {kw.lower(): 0 for kw in keywords}  # O = (keywrds)

    # O = (reviews * keywords)
    for kw in aggr:
        for p in reviews:
            aggr[kw] += len(re.findall(kw, p, flags=re.IGNORECASE)) != 0

    h = []
    for w, cnt in aggr.items():
        if cnt == 0:
            continue
        obj = HeapObj(word=w, cnt=cnt)
        heapq.heappush(h, obj)
        if len(h) > k:
            heapq.heappop(h)
    return [obj.word for obj in sorted(h, reverse=True)]


assert top_freq_words(2, ["anacell", "cetracular", "betacellular"], [
    "Anacell provides the best services in the city",
    "betacellular has awesome services",
    "Best services provided by anacell, everyone should use anacell",
]) == ["anacell", "betacellular"]

assert top_freq_words(2, ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"], [
    "I love anacell Best services; Best services provided by anacell",
    "betacellular has great services",
    "deltacellular provides much better services than betacellular",
    "cetracular is worse than anacell",
    "Betacellular is better than deltacellular.",
]) == ["betacellular", "anacell"]
