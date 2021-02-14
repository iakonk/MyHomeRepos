class Solution(object):
    def get_square(self, num):
        res = 0
        while num:
            num, digit = num // 10, num % 10
            res += digit*digit
        return res

    def is_num_happy(self, num):
        """ it will either stuck on 1 loop or other number """
        slow = self.get_square(num)
        fast = self.get_square(self.get_square(num))
        while True:
            if fast == slow:
                break
            slow = self.get_square(slow)
            fast = self.get_square(self.get_square(fast))
        return slow == 1


assert Solution().is_num_happy(23)
assert not Solution().is_num_happy(12)
