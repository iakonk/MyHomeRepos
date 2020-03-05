class Solution(object):
    def next_number(self, n):
        total_sum = 0
        while n != 0:
            n, last_digit = divmod(n, 10)
            total_sum += last_digit**2
        return total_sum

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        while n != 1 and n not in seen:
            n = self.next_number(n)
            seen.add(n)
        return n == 1


assert Solution().isHappy(19)