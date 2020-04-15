class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = start = 0
        while start < len(s):
            if start + 1 < len(s) and values[s[start]] < values[s[start + 1]]:
                total += values[s[start + 1]] - values[s[start]]
                start += 2
            else:
                total += values[s[start]]
                start += 1
        return total


# ans = Solution().romanToInt("III")
ans = Solution().romanToInt("MCMXCIV")
print(ans)
