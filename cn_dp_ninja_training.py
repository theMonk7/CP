from typing import *


def ninjaTraining(n: int, points: List[List[int]]) -> int:
    act_num = 3
    last = 3
    dp = [[-1 for i in range(act_num + 1)] for j in range(n)]

    return td(points, n - 1, last, dp, act_num)


def td(points, n, last, dp, act_num):
    if n == 0:
        m = 0
        for i in range(act_num):
            if i != last:
                m = max(m, points[0][i])
        dp[0][last] = m
        return m
    if dp[n][last] != -1:
        return dp[n][last]
    maxi = 0
    for i in range(act_num):
        if i != last:
            p = td(points, n - 1, i, dp, act_num)
            maxi = max(maxi, p)

    dp[n][last] = maxi
    print(dp)
    return maxi


print(ninjaTraining(3, [[10, 40, 70], [20, 50, 80], [30, 90, 60]]))
