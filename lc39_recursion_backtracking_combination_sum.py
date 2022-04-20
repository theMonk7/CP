class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        self.count(candidates, len(candidates), target, 0, [], res)
        return res

    def count(self, arr, n, t, i, temp, res):
        if i >= n:
            return

        if t == 0:
            res.append(temp)
            return
        if arr[i] <= t:
            temp.append(arr[i])
            self.count(arr, n, t - arr[i], i, temp[:], res)
            temp.pop()
        self.count(arr, n, t, i + 1, temp[:], res)

ar = [2,3,4,5,6]
t = 8

print(Solution().combinationSum(ar,t))