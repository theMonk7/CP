class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:

        arr = list(range(k, num + 1, 10))
        if num == 0 and k != 0 or num == 0 and k == 0:
            return 0
        if k == 0 and num < 10:
            return -1
        elif k == 0 and num >= 10:
            arr = arr[1:]

        tar = num
        res = []
        dp = [[-1] * (tar + 1) for i in range(len(arr) + 1)]
        r = self.calc(arr, tar, len(arr), [], res, dp)
        return r if r != 10000000000000000000 else -1

    def calc(self, arr, tar, n, temp, res, dp):
        if n == 0:
            if tar == 0:
                return 1
            else:
                return 10000000000000000000
        if tar == 0:
            res.append(len(temp))
            return len(temp)
        if dp[n][tar] != -1:
            return dp[n][tar]
        take = 10000000000000000000
        not_take = self.calc(arr, tar, n - 1, temp, res,dp)
        if arr[n - 1] <= tar:
            take = self.calc(arr, tar - arr[n - 1], n, temp + [arr[n - 1]], res,dp)
        dp[n][tar] = min(take, not_take)
        return dp[n][tar]
print(Solution().minimumNumbers(20,1))