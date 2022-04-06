class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.returnIndex(nums, 0, len(nums) - 1, target)

    def returnIndex(self, nums, low, high, val):
        if low < high:
            mid = (low + high) // 2

            if nums[mid] == val:
                return mid

            elif nums[mid] > val:
                return self.returnIndex(nums, low, mid - 1, val)
            else:
                return self.returnIndex(nums, mid + 1, high, val)
        else:
            if nums[low] == val:
                return low
            elif nums[low] < val:
                return low + 1
            else:
                return low


print(Solution().searchInsert([1,3,5,6], 0))