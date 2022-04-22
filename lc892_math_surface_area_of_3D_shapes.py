class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        area = 0
        common = 0
        n = len(grid)
        for r in range(n):
            for c in range(n):
                if grid[r][c] != 0: area += 4 * grid[r][c] + 2
                if r - 1 >= 0: common += min(grid[r - 1][c], grid[r][c])
                if r + 1 < n: common += min(grid[r + 1][c], grid[r][c])
                if c - 1 >= 0: common += min(grid[r][c - 1], grid[r][c])
                if c + 1 < n: common += min(grid[r][c + 1], grid[r][c])
        return area - common
