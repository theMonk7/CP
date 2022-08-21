import math


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l = 1
        r = max(piles)

        while l < r:
            m = (l + r) // 2
            if self.check(piles, m) < h:
                r = m
            else:
                l = m + 1
        return l

    def check(self, piles, k):
        time = 0
        for pile in piles:
            time += math.ceil(pile / k)
        return time

print(Solution().minEatingSpeed(
[312884470],
312884469))