class Solution:
    def maxIncreaseKeepingSkyline(self, grid: list[list[int]]) -> int:
        r_max = [max(e) for e in grid]
        c_max = [max(e) for e in zip(*grid)]
        s = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                s += abs(grid[r][c] - min(r_max[r],c_max[c]))
        return s