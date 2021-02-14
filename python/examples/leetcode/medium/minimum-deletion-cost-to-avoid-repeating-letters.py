class Solution(object):
    def minCost(self, s, cost):
        if len(s) <= 1:
            return 0
        ans = prev = 0
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                prev = i
            else:
                ans += min(cost[i], cost[prev])
                if cost[i] > cost[prev]:
                    prev = i
        return ans


ans = Solution().minCost("abaac", [1,2,3,4,5])
assert ans == 3

ans = Solution().minCost("aabaa", [1,2,3,4,1])
assert ans == 2

ans = Solution().minCost("aaabbbabbbb", [3,5,10,7,5,3,5,5,4,8,1])
assert ans == 26


