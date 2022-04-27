class Solution:
    def search(self, nums: list[int], target: int) -> int:
        pivot = self.find_pivot(nums)
        ans = -1
        if pivot == -1:
            return self.bin_search(nums, target, 0, len(nums) - 1)
        else:
            ans = self.bin_search(nums, target, 0, pivot)
            if ans == -1:
                ans = self.bin_search(nums, target, pivot + 1, len(nums) - 1)
        return ans

    def bin_search(self, nums: list[int], target: int, l: int, h: int) -> int:

        while l <= h:
            m = (l + h) // 2
            if nums[m] == target:
                return m
            elif target > nums[m]:
                l = m + 1
            else:
                h = m - 1
        return -1

    def find_pivot(self, nums: list[int]) -> int:

        l = 0
        h = len(nums) - 1
        while l < h:
            m = (l + h) // 2
            if nums[m] > nums[m + 1]:
                return m
            elif nums[m] < nums[m - 1]:
                return m - 1
            elif nums[m] <= nums[l]:
                h = m - 1
            elif nums[m] > nums[l]:
                l = m + 1
        return -1
