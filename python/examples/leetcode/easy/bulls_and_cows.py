
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        import collections

        s, g = collections.Counter(secret), collections.Counter(guess)
        bulls = sum(sd == gd for sd, gd in zip(secret, guess))
        cows = sum((s & g).values()) - bulls
        return '{}A{}B'.format(bulls, cows)


ans = Solution().getHint("113", "301")
print(ans)