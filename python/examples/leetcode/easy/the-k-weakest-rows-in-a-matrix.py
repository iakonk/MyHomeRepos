"""
Given a m * n matrix mat of ones (representing soldiers) and zeros (representing civilians),
return the indexes of the k weakest rows in the matrix ordered from the weakest to the strongest.

A row i is weaker than row j, if the number of soldiers in row i is less than the number of soldiers in row j,
or they have the same number of soldiers but i is less than j. Soldiers are always stand in the frontier of a row,
that is, always ones may appear first and then zeros.
"""
import heapq
from heapq import nsmallest


class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        O( n*log(m) + n*log(k) )
        """

        def soldiers_num(row):
            start, end = 0, len(row)
            while start < end:
                mid = start + (end - start) // 2
                if row[mid] == 0:
                    end = mid
                else:
                    start = mid + 1
            return start

        h = []
        for i in range(k):
            s = soldiers_num(mat[i])
            heapq.heappush(h, (-s, i))
        print(h)

        for i in range(k, len(mat)):
            s = soldiers_num(mat[i])
            if -s > h[0][0]:
                heapq.heappop(h)
                heapq.heappush(h, (-s, i))
        print(h)
        # return [idx for _, idx in nsmallest(k, [(soldiers_num(row), idx) for idx, row in enumerate(mat)])]
        # h = []
        # for idx, row in enumerate(mat):
        #     s = soldiers_num(row)
        #     heapq.heappush(h, (s, idx))
        # return [idx for _, idx in sorted(h)][:k]
        # ans = sorted([(soldiers_num(row), idx) for idx, row in enumerate(mat)])[:k]
        # return [idx for _, idx in ans]

#  [2,0,3,1,4]
mat = [[1, 1, 0, 0, 0],  # 2 0
       [1, 1, 1, 1, 0],  # 4 1
       [1, 0, 0, 0, 0],  # 1 2
       [1, 1, 0, 0, 0],  # 2 3
       [1, 1, 1, 1, 1]]  # 5 4
k = 3
assert Solution().kWeakestRows(mat, k) == [2, 0, 3]

mat = [[1, 0, 0, 0],
       [1, 1, 1, 1],
       [1, 0, 0, 0],
       [1, 0, 0, 0]]
k = 2
# ans = Solution().kWeakestRows(mat, k)
# assert ans == [0, 2], ans
