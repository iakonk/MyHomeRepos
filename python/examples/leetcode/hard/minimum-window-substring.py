import collections


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if s and not t:
            return ""

        ans = ""
        tail, match = 0, 0
        aggr_t = collections.Counter(t)

        for head, char in enumerate(s):
            if char in aggr_t:
                aggr_t[char] -= 1
                match += aggr_t[char] == 0

            # because {a: 2} -> match = 1
            while match >= len(aggr_t):
                # Save the smallest window until now.
                if head - tail + 1 < len(ans) or ans == "":
                    ans = s[tail: head + 1]
                #  put char back and decrement match
                if s[tail] in aggr_t:
                    # if s[tail]< 0 it means one more left_char is ahead
                    # and this dup did not affect match
                    match -= aggr_t[s[tail]] == 0
                    aggr_t[s[tail]] += 1
                # shrink the window
                tail += 1
        return ans


ans = Solution().minWindow("ADOBECODEBANC", "ABC")
assert ans == "BANC"

ans = Solution().minWindow("bdab", "ab")
assert ans == 'ab'

ans = Solution().minWindow("aa", "aa")
assert ans == 'aa'


# optimized
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if s and not t:
            return ""

        ans = ""
        stack = []

        for head, char in enumerate(s):
            if char in t:
                stack.append(head)
        w_size = len(t)
        print(stack, t)
        for i in range(0, len(stack), w_size):

            if i + w_size - 1 > len(stack):
                head_i = stack[i]
                tail_i = stack[i-1]
            else:
                tail_i = stack[i]
                head_i = stack[i + w_size - 1]
            print(i, head_i, tail_i)
            if head_i - tail_i + 1 < len(ans) or not ans:
                ans = s[tail_i:head_i + 1]

        return ans


ans = Solution().minWindow("ADOBECODEBANC", "ABC")
assert ans == "BANC"

ans = Solution().minWindow("bdab", "ab")
assert ans == 'ab'

ans = Solution().minWindow("aa", "aa")
assert ans == 'aa'
