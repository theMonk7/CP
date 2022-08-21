import sys
from typing import *


def frogJump(n: int, heights: List[int]) -> int:
    dp = [-1] * (n + 1)
    return __solver(n - 1, heights, dp)


def __solver(n: int, heights: list[int], dp: list[int]) -> int:
    if n == 0:
        dp[n] = 0
        return 0
    if n == 1:
        dp[n] = abs(heights[n] - heights[n - 1])
        return dp[n]
    if dp[n] != -1:
        return dp[n]

    dp[n] = min(__solver(n - 1, heights, dp) + abs(heights[n] - heights[n - 1]),
                __solver(n - 2, heights, dp) + abs(heights[n] - heights[n - 2]))
    print(dp)
    return dp[n]


def dp_top_down(heights, n):
    dp = [0] * n
    dp[0] = 0
    dp[1] = abs(heights[1] - heights[0])
    for i in range(2, n):
        dp[i] = min(dp[i - 1] + abs(heights[i] - heights[i - 1]), dp[i - 2] + abs(heights[i] - heights[i - 2]))
    print(dp)
    return dp[n - 1]


def frog_jump_k_jumps(heights, n, k, dp):
    if n <= 0:
        return 0
    if dp[n] != -1:
        return dp[n]
    m = sys.maxsize
    for i in range(1, k + 1):
        if n - i >= 0:
            t = frog_jump_k_jumps(heights, n - i, k, dp) + abs(heights[n] - heights[n - i])
            m = min(m, t)
    dp[n] = m

    return m


heights = [40, 10, 20, 70, 80, 10, 20, 70, 80, 60]
# heights = [int(e) for e in heights]
n = len(heights)
# print(frogJump(n ,heights ))
# print(dp_top_down(heights, n))
dp = [-1]*(n+1)
print(frog_jump_k_jumps(heights, n-1, 4, dp))

