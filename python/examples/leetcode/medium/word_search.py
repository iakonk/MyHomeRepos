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
        if not suffix:
            return True

        if r < 0 or r >= self.R or 0 > c or c == self.C or self.board[r][c] != suffix[0]:
            return False

        res = False
        for r_offset, c_offset in ((0, 1), (1, 0), (-1, 0), (0, -1)):
            res = self.backtrack(r+r_offset, c+c_offset, suffix[1:])
            if res: break

        return res