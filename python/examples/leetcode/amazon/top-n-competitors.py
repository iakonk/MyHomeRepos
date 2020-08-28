import re
import heapq


class HeapqObj(object):
    def __init__(self, word, cnt):
        self.word = word
        self.cnt = cnt

    def __lt__(self, other):
        """ if cnt is equal for ['newshop', 'shopnow'],
            put shopnow on top of heap as a smallest object
        """
        return (self.cnt < other.cnt) or self.cnt == other.cnt and self.word > other.word

    def __str__(self):
        return self.word

import operator
def topCompetitors(topNCompetitors, competitors, reviews):
    aggr = {cmp: 0 for cmp in competitors}
    for cmp in competitors:
        for rev in reviews:
            #  use re to find a match, because competitor may appear in a review as: 'cmp,' or 'Cmp'
            match = re.findall(cmp, rev, re.IGNORECASE)
            aggr[cmp] += len(match)
            # if match:

    print(aggr)
    heap = []
    for cmp, cnt in aggr.items():
        obj = HeapqObj(cmp, cnt)
        heapq.heappush(heap, obj)
        print([(obj.word, obj.cnt) for obj in heap])
        if len(heap) > topNCompetitors:
            heapq.heappop(heap)

    print([(obj.word, obj.cnt )for obj in sorted(heap, reverse=True, key=operator.attrgetter('cnt'))])
    return [obj.word for obj in sorted(heap, reverse=True, key=operator.attrgetter('cnt'))]


# ans = topCompetitors(2,
#                      ['newshop', 'mymarket', 'shopnow'],
#                      ['newshop is newshop', 'shopnow shopnow', 'mymarket is gre mymarket mymarket mymarket', 'dsfhds'])
# assert ans == ['mymarket', 'newshop'], ans
#

comp = [
"anacell",
"betacellular",
"cetracular",
"deltacellular",
"eurocell",
]
rev = [
"I love anacell Best services provided by anacell in the town",
"betacellular has great services",
"deltacellular provides much better services than betacellular",
"cetracular is worse than eurocell",
"betacellular is better than deltacellular",
]

ans = topCompetitors(2, comp, rev)
print(ans)