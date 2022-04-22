class Solution1:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        res: list[list[list[str]]] = []
        self.__solver_logic(board, 0, 0, res)
        print(res)
        for i in range(9):
            board.insert(0, res[0][9 - i - 1])
            board.pop()

    def __solver_logic(self, board: list[list[str]], row, col, res):
        if row == 9:
            res.append(board)
            return
        if board[row][col] == ".":
            for i in range(1, 10):
                if self.__isValid(val=i, row=row, col=col, board=board):
                    board[row][col] = str(i)
                    if col == 8:
                        self.__solver_logic([r[:] for r in board], row + 1, 0, res)
                    else:
                        self.__solver_logic([r[:] for r in board], row, col + 1, res)
                    board[row][col] = "."
        else:
            if col == 8:
                self.__solver_logic([r[:] for r in board], row + 1, 0, res)
            else:
                self.__solver_logic([r[:] for r in board], row, col + 1, res)

    def __isValid(self, val: int, row: int, col: int, board: list[list[str]]) -> bool:
        for i in range(9):
            if board[row][i] == str(val):
                return False
            if board[i][col] == str(val):
                return False
        rx = ry = 0
        cx = cy = 0
        if row in range(3) and col in range(3):
            rx, ry, cx, cy = 0, 3, 0, 3
        elif row in range(3) and col in range(3, 6):
            rx, ry, cx, cy = 0, 3, 3, 6
        elif row in range(3) and col in range(6, 9):
            rx, ry, cx, cy = 0, 3, 6, 9
        elif row in range(3, 6) and col in range(3):
            rx, ry, cx, cy = 3, 6, 0, 3
        elif row in range(3, 6) and col in range(3, 6):
            rx, ry, cx, cy = 3, 6, 3, 6
        elif row in range(3, 6) and col in range(6, 9):
            rx, ry, cx, cy = 3, 6, 6, 9
        elif row in range(6, 9) and col in range(3):
            rx, ry, cx, cy = 6, 9, 0, 3
        elif row in range(6, 9) and col in range(3, 6):
            rx, ry, cx, cy = 6, 9, 3, 6
        elif row in range(6, 9) and col in range(6, 9):
            rx, ry, cx, cy = 6, 9, 6, 9
        for r in range(rx, ry):
            for c in range(cx, cy):
                if board[r][c] == str(val):
                    return False
        return True


s_board: list[list[str]] = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

# Solution1().solveSudoku(s_board)


# ------------------------------------------------------------------------------------------------------
# SUDOKU SOLVER Method 2
# ------------------------------------------------------------------------------------------------------

class Solution2:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.__solver(board)
        print(board)

    def __solver(self, board: list[list[str]]) -> bool:

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == ".":
                    for i in range(1, 10):
                        if self.__is_valid(board, r, c, str(i)):
                            board[r][c] = str(i)
                            if self.__solver(board):
                                return True
                            else:
                                board[r][c] = "."
                    return False
        return True

    def __is_valid(self, board: list[list[str]], row: int, col: int, val: str) -> bool:
        for i in range(9):
            if board[row][i] == val:
                return False
            if board[i][col] == val:
                return False
            if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == val:
                return False
        return True

Solution2().solveSudoku(s_board)