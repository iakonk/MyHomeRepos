class Solution(object):
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        r_min = {min(row) for row in matrix}
        c_max = {max(col) for col in zip(*matrix)}
        return list(r_min & c_max)


matrix = [[3,7,8], [9,11,13], [15,16,17]]
ans = Solution().luckyNumbers(matrix)
assert ans == [15]
