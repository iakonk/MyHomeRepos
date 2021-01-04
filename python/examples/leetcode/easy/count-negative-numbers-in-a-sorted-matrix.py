"""
Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise.
Return the number of negative numbers in grid.
"""


class Solution(object):
    def countNegatives(self, grid):

        def binary_search(row):
            start, end = 0, len(row)
            while start < end:
                mid = start + (end - start) // 2
                if row[mid] < 0:
                    end = mid
                else:
                    start = mid + 1
            return len(row) - start

        return sum([binary_search(row) for row in grid])


ans = Solution().countNegatives([[4, 3, 2, -1],
                                 [3, 2, 1, -1],
                                 [1, 1, -1, -2],
                                 [-1, -1, -2, -3]])
assert ans == 8, ans

ans = Solution().countNegatives([[3, 2], [1, 0]])
assert ans == 0
