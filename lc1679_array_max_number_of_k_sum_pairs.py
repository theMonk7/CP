class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        nums.sort()
        l = 0
        r = len(nums) - 1
        cnt = 0
        while l < r:
            s = nums[l] + nums[r]
            if s < k:
                l += 1
            elif s > k:
                r -= 1
            else:
                cnt += 1
                l += 1
                r -= 1
        return cnt