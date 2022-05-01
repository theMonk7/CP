class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []
        self.find_comb(n, k, res, [], 0)
        return res

    def find_comb(self, n: int, k: int, res: list[list[int]], temp: list[int], index: int):

        if len(temp) == k:
            res.append(temp)
            return
        for i in range(index, n):
            temp.append(i + 1)
            self.find_comb(n, k, res, temp[:], i + 1)
            temp.pop()
# NOTE : The nCk , ie a combination of k elements from
# n total elements is a subset of the set of subsets
# SUBSET ([1,2,3]) = {[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]}
# Combination 3C2 = {[1,2],[1,3],[2,3]}
print(Solution().combine(4,3))