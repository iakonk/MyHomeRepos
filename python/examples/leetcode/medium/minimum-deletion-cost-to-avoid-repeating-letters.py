"""
https://leetcode.com/problems/minimum-deletion-cost-to-avoid-repeating-letters/

Given a string s and an array of integers cost where cost[i] is the cost of deleting the ith character in s.
Return the minimum cost of deletions such that there are no two identical letters next to each other.

Notice that you will delete the chosen characters at the same time,
in other words, after deleting a character, the costs of deleting other characters will not change.
"""


class Solution(object):
    def minCost(self, s, cost):
        if len(s) <= 1:
            return 0
        ans = prev = 0
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                prev = i
            else:
                ans += min(cost[i], cost[prev])
                if cost[i] > cost[prev]:
                    prev = i
        return ans


ans = Solution().minCost("abaac", [1, 2, 3, 4, 5])
assert ans == 3

ans = Solution().minCost("aabaa", [1, 2, 3, 4, 1])
assert ans == 2

ans = Solution().minCost("aaabbbabbbb", [3, 5, 10, 7, 5, 3, 5, 5, 4, 8, 1])
assert ans == 26
