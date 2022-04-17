class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        mi = 1000000
        for i in range(len(nums)-k + 1):
            if nums[i + k -1] - nums[i] < mi:
                mi = nums[i + k - 1] - nums[i]
        return mi