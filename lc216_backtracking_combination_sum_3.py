class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        res = []
        self.helper(k, n, [], res, 1)
        return res

    def helper(self, k: int, n: int, temp: list[int], res: list[list[int]], ind):
        if n < 0:
            return
        if len(temp) == k:
            if n == 0:
                res.append(temp)
                return
            else:
                return
        for i in range(ind, 10):
            self.helper(k, n - i, temp + [i], res, i + 1)
