"""
You are given an integer n, the number of teams in a tournament that has strange rules:

If the current number of teams is even, each team gets paired with another team. A total of n / 2 matches are played,
and n / 2 teams advance to the next round.
If the current number of teams is odd, one team randomly advances in the tournament, and the rest gets paired.
A total of (n - 1) / 2 matches are played, and (n - 1) / 2 + 1 teams advance to the next round.
Return the number of matches played in the tournament until a winner is decided.

"""


class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        def rec(teams):
            if not teams // 2:
                return 0
            elif teams % 2 == 0:
                return teams / 2 + rec(teams /2)
            else:
                return (teams - 1) / 2 + rec((teams-1)/2+1)

        return int(rec(n))


ans = Solution().numberOfMatches(14)
assert ans == 13

ans = Solution().numberOfMatches(7)
assert ans == 6
