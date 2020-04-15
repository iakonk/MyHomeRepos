class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        a, b = str(a), str(b)
        max_len, min_len = max(len(a), len(b)), min(len(a), len(b))
        a.zfill(max_len - min_len)
        b.zfill(max_len - min_len)

        res = []
        overflow = 0
        for i, j in zip(a, b):
            sum_ = int(i) + int(j) + overflow

            # overflow, last = divmod(sum_, 10)
            # res.append(last)
            # print(i, j, sum_, overflow, a, b)
        # if overflow:
        #     res.append(overflow)
        res = reversed(res)

        return int(''.join([str(d) for d in res])) if res else 0


ans = Solution().getSum(24, 39)
print(ans)