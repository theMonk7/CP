class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        board = [[0] * n for i in range(m)]
        for x, y in ops:
            for r in range(m):
                for c in range(n):
                    if r < x and c < y:
                        board[r][c] += 1
        mu = max([max(r) for r in board])
        cnt = 0
        print(board)
        for r in range(m):
            for c in range(n):
                if board[r][c] == mu:
                    cnt += 1
        return cnt

    def maxCount_better(self, m: int, n: int, ops: list[list[int]]) -> int:
        if len(ops) == 0: return m * n
        import math
        min_x = math.inf
        min_y = math.inf
        for x, y in ops:
            if x < min_x:
                min_x = x
            if y < min_y:
                min_y = y
        return min_x * min_y


print(Solution().maxCount(3, 3, [[2, 2], [3, 3], [3, 3], [3, 3], [2, 2], [3, 3], [3, 3], [3, 3], [2, 2], [3, 3], [3, 3],
                                 [3, 3]]))
