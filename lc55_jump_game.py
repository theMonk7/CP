class Solution:
    def canJump(self, nums: list[int]) -> bool:
        dp = [-1] * (len(nums))
        return self.rec(nums, len(nums), 0, dp)

    def rec(self, nums, n, ind, dp):
        if ind >= n:
            return False
        if ind == n - 1:
            dp[ind] = True
            return True
        if dp[ind] != -1:
            return dp[ind]

        for i in range(1, nums[ind] + 1):
            jump = self.rec(nums, n, ind + i, dp)

            print(dp)
            if jump:
                dp[ind] = True
                return True
        dp[ind] = False
        print(dp)
        return False


# print(Solution().canJump([3, 2, 1, 1, 4]))
o = [2, 3, 4]


def arrayChange(nums: list[int], operations: list[list[int]]) -> list[int]:
    hm = {}
    for i in range(len(operations)):
        hm[operations[i][0]] = [operations[i][1], i]
    c = 0
    l = -1
    for i in range(len(nums)):
        while hm.__contains__(nums[i]) and hm[nums[i]][1] > l:
            k = nums[i]
            l = hm[nums[i]][1]
            nums[i] = hm[nums[i]][0]
            del hm[k]
        l = -1
    return nums


# print(arrayChange([1,2],[[1,3],[2,1],[3,2]]))


def subsetSumToK(n, k, arr):
    dp = [[-1] * (k + 1) for i in range(n + 1)]
    ans = helper(n, k, arr, dp)
    print(dp)

    # Write your code here
    # Return a boolean variable 'True' or 'False' denoting the answer


def helper(n, k, arr, dp):
    if n == 0:
        if k == 0:
            dp[n][k] = True
            return True
        else:
            dp[n][k] = False
            return False
    if k == 0:
        dp[n][k] = True
        return True
    if dp[n][k] != -1:
        return dp[n][k]

    not_take = helper(n - 1, k, arr, dp)
    take = False
    if not_take:
        dp[n][k] = True
        return True
    else:
        if arr[n - 1] <= k:
            take = helper(n - 1, k - arr[n - 1], arr, dp)
            dp[n][k] = take
            return dp[n][k]
        else:
            dp[n][k] = False
            return False


# print(subsetSumToK(10, 45, [11, 82, 91, 97, 87, 42, 80, 10, 42, 42]))


from typing import List


def countPartitions(n: int, d: int, arr: List[int]) -> int:
    s1 = sum(arr)
    s2 = abs(s1 - d)
    if s2 % 2 == 0:
        s = s2 // 2
    else:
        return 0
    dp = [[0] * (s + 1) for i in range(n + 1)]
    for i in range(s + 1):
        dp[0][i] = 0
    dp[0][0] = 1
    num_zero = 0
    for i in range(1, n + 1):
        if arr[i - 1] == 0:
            num_zero += 1
        dp[i][0] = 2 ** num_zero

    for i in range(1, n + 1):
        for j in range(1, s + 1):
            not_take = dp[i - 1][j]
            take = 0
            if arr[i - 1] <= j:
                take = dp[i - 1][j - arr[i - 1]]
            dp[i][j] = (take + not_take) % (10 ** 9 + 7)
    print(dp)
    return dp[n][s]


print(countPartitions(6, 17, [1, 0, 8, 5, 1, 4]))
