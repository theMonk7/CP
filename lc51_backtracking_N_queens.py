class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        self.__instantiate_hashes(n)
        board = [["."] * n for _ in range(n)]
        self.queen_solver(board, 0, len(board), res)
        ans = [["".join(r) for r in sol] for sol in res]
        return ans

    def queen_solver(self, board, col, n, res):
        if col == n:
            res.append(board)
            return
        for row in range(n):
            if not self.horizontal_hash[row] and not self.bottom_up_hash[row+col] and not self.tob_bottom_hash[n-1+row-col]:
                board[row][col] = "Q"
                self.horizontal_hash[row] = True
                self.bottom_up_hash[row+col] = True
                self.tob_bottom_hash[n-1+row-col] = True
                self.queen_solver([r[:] for r in board], col + 1, n, res)
                board[row][col] = "."
                self.horizontal_hash[row] = False
                self.bottom_up_hash[row + col] = False
                self.tob_bottom_hash[n - 1 + row - col] = False

    def __is_safe(self, board, row, col, n):
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

    def __instantiate_hashes(self,n):
        self.horizontal_hash = dict([(i, False) for i in range(n)])
        self.bottom_up_hash = dict([(i, False) for i in range(2*(n-1)+1)])
        self.tob_bottom_hash = dict([(i, False) for i in range(2*(n-1)+1)])

    def is_safe_optimised_hashing(self, r: int, c: int) -> bool:
        pass


print(Solution().solveNQueens(4))
