class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        res = []
        self.back(nums, target, res, [])
        return res

    def back(self, arr, t, res, temp):
        if t == 0:
            res.append(temp)
            return
        for i in range(0, len(arr)):
            if arr[i] <= t:
                self.back(arr, t - arr[i], res, temp + [arr[i]])

print(Solution().combinationSum4([4,2,1],15))