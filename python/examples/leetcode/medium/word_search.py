# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
#
# Example:
#
# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
#
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.


class Solution(object):

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.board = board
        self.R, self.C = len(board), len(board[0])
        for r in range(0, self.R):
            for c in range(0, self.C):
                if self.backtrack(r, c, word):
                    return True
        return False

    def backtrack(self, r, c, suffix):
        if len(suffix) == 0:
            return True

        if r < 0 or r == self.R or 0 > c or c == self.C or self.board[r][c] != suffix[0]:
            return False

        res = False
        self.board[r][c] = "#"
        for r_offset, c_offset in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            res = self.backtrack(r+r_offset, c+c_offset, suffix[1:])
            if res: break

        self.board[r][c] = suffix[0]
        return res