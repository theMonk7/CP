class Solution:
    def minimumAverageDifference(self, nums: list[int]) -> int:
        min_ind = -1
        min_diff = 10000000000000000000000000
        l_sum = 0
        s = sum(nums)
        n = len(nums)
        for i in range(n):
            if i != len(nums) - 1:
                l_sum += nums[i]
                avg = abs(l_sum // (i + 1) - (s - l_sum) // (n - i - 1))
            else:
                avg = abs(s // (i + 1))

            if avg < min_diff:
                min_diff = avg
                min_ind = i
        return min_ind
