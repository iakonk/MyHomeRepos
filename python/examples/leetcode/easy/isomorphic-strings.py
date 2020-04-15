class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # if len(s) != len(t):
        #     return False
        #
        # set_s, set_t = {}, {}
        # s_start = t_start = 0
        # for ind in range(len(s)):
        #     rigt_s_char, right_t_char = s[ind], t[ind]
        #
        #     set_s.setdefault(rigt_s_char, 0)
        #     set_s[rigt_s_char] += 1
        #     set_t.setdefault(right_t_char, 0)
        #     set_t[right_t_char] += 1
        #
        #     while len(set_s) > 1:
        #         left_s_char = s[s_start]
        #         set_s[left_s_char] -= 1
        #         if set_s[left_s_char] <= 0:
        #             del set_s[left_s_char]
        #         s_start += 1
        #
        #     while len(set_t) > 1:
        #         left_t_char = t[t_start]
        #         set_t[left_t_char] -= 1
        #         if set_t[left_t_char] <= 0:
        #             del set_t[left_t_char]
        #         t_start += 1
        #
        #     if s_start != t_start:
        #         return False
        # return True

        d1, d2 = dict(), dict()
        for v, w in zip(s,t):
            print(d1, d2, v, w)
            if (v in d1 and d1[v] != w) or (w in d2 and d2[w] != v):
                return False
            d1[v], d2[w] = w, v
        return True

ans = Solution().isIsomorphic('foo', 'bar')
print(ans)

ans = Solution().isIsomorphic('foof', 'baac')
print(ans)


