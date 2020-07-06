"""
https://leetcode.com/problems/surrounded-regions/
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.
"""


class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])

        def mark_board(i, j):
            if not 0 <= i < m or not 0 <= j < n:
                return
            if board[i][j] == "O":
                board[i][j] = ""
                mark_board(i + 1, j)
                mark_board(i - 1, j)
                mark_board(i, j + 1)
                mark_board(i, j - 1)

        for i in range(m):
            mark_board(i, 0)
            mark_board(i, n - 1)
        for j in range(n):
            mark_board(0, j)
            mark_board(m - 1, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == '':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'
        return board


board = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"]
]
ans = Solution().solve(board)
print(ans)
