"""
https://leetcode.com/problems/search-suggestions-system/

Given an array of strings products and a string searchWord.
We want to design a system that suggests at most three product names from products after each
character of searchWord is typed. Suggested products should have common prefix with the searchWord.
If there are more than three products with a common prefix return the three lexicographically minimums products.

Return list of lists of the suggested products after each character of searchWord is typed.



Example 1:

Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
Explanation: products sorted lexicographically = ["mobile","moneypot","monitor","mouse","mousepad"]
After typing m and mo all products match and we show user ["mobile","moneypot","monitor"]
After typing mou, mous and mouse the system suggests ["mouse","mousepad"]
"""
import heapq


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


class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """

        def search():
            aggr = {}
            for pr in products:
                if pr.startswith(prefix):
                    aggr.setdefault(pr, 0)
                    aggr[pr] += 1

            h = []
            for w, cnt in aggr.items():
                obj = HeapObj(word=w, cnt=cnt)
                heapq.heappush(h, obj)
                if len(h) > 3:
                    heapq.heappop(h)
            return [obj.word for obj in sorted(h, reverse=True)]

        matches = []
        prefix = ''
        for char in searchWord:
            prefix += char
            words = search()
            matches.append(words)
        return matches


products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
searchWord = "mouse"
ans = Solution().suggestedProducts(products, searchWord)
assert ans == [
    ["mobile", "moneypot", "monitor"],
    ["mobile", "moneypot", "monitor"],
    ["mouse", "mousepad"],
    ["mouse", "mousepad"],
    ["mouse", "mousepad"]
]
