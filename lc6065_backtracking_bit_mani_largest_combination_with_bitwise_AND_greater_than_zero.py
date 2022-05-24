class Solution:
    m = 0

    def largestCombination(self, candidates: list[int]) -> int:
        candidates.sort()
        self.helper(candidates, 0, [])
        return self.m

    def helper(self, nums, ind, temp):
        if len(temp) > 0:
            k = temp[0]
            for i in range(1, len(temp)):
                k &= temp[i]
            if k <= 0:
                return
            else:
                if len(temp) > self.m:
                    self.m = len(temp)

        for i in range(ind, len(nums)):
            if i > ind and nums[i] == nums[i - 1]:
                continue
            self.helper(nums, i + 1, temp + [nums[i]])

print(Solution().largestCombination([84,40,66,44,91,90,1,14,73,51,47,35,18,46,18,65,55,18,16,45,43,58,90,92,91,43,44,76,85,72,24,89,60,94,81,90,86,79,84,41,41,28,44]))