class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.helper(candidates, len(candidates), 0, [], res, target)
        return res

    def helper(self, arr, n, i, temp, res, tar):
        if tar == 0:
            res.append(temp)
            return
        for k in range(i, n):
            if k > i and arr[k] == arr[k - 1]:
                continue
            if tar < arr[k]:
                break
            temp.append(arr[k])
            self.helper(arr, n, k + 1, temp[:], res, tar - arr[k])
            temp.pop()

arr = [0,0,1,0,1]
t = 2

print(Solution().combinationSum2(arr,t))