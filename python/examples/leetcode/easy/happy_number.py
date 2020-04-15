class Solution(object):
    def next_number(self, n):
        if n == 0:
            return 0
        else:
            all_but_last, last = divmod(n, 10)
            return last ** 2 + self.next_number(all_but_last)


    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = self.next_number(n)

        return n == 1


assert Solution().isHappy(19)