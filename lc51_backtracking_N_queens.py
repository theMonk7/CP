class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        board = [["."] * n for _ in range(n)]
        self.queen_solver(board, 0, len(board), res)
        ans = [["".join(r) for r in sol] for sol in res]
        return ans

    def queen_solver(self, board, col, n, res):
        if col == n:
            res.append(board)
            return
        for row in range(n):
            if self.is_safe(board, row, col, n):
                board[row][col] = "Q"
                self.queen_solver([r[:] for r in board], col + 1, n, res)
                board[row][col] = "."

    def is_safe(self, board, row, col, n):
        row_cpy = row
        col_cpy = col
        while col_cpy >= 0:
            if board[row_cpy][col_cpy] != ".":
                return False
            col_cpy -= 1
        row_cpy = row
        col_cpy = col
        while col_cpy >= 0 and row_cpy >= 0:
            if board[row_cpy][col_cpy] != ".":
                return False
            col_cpy -= 1
            row_cpy -= 1

        row_cpy = row
        col_cpy = col
        while col_cpy >= 0 and row_cpy < n:
            if board[row_cpy][col_cpy] != ".":
                return False
            col_cpy -= 1
            row_cpy += 1

        return True


print(Solution().solveNQueens(4))
