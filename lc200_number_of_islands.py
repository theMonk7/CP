class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        r = len(grid)
        c = len(grid[0])
        cnt = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1":
                    self.g_dfs(i, j, grid, r, c)
                    print(grid)
                    cnt += 1

        return cnt

    def g_dfs(self, i, j, grid, r, c):
        grid[i][j] = "0"
        if i > 0:
            if grid[i - 1][j] == "1":
                self.g_dfs(i - 1, j, grid, r, c)
        if i < r - 1:
            if grid[i + 1][j] == "1":
                self.g_dfs(i + 1, j, grid, r, c)
        if j > 0:
            if grid[i][j - 1] == "1":
                self.g_dfs(i, j - 1, grid, r, c)
        if j < c - 1:
            if grid[i][j + 1] == "1":
                self.g_dfs(i, j + 1, grid, r, c)

print(Solution().numIslands(
    [["1","1","1","1","0"],
     ["1","1","0","1","0"],
     ["1","1","0","0","0"],
     ["0","0","0","0","0"]]))
