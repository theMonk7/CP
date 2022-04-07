class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = sum(nums)
        l_sum = nums[0]
        if s == l_sum:
            return 0
        for i in range(1, len(nums)):
            s -= nums[i - 1]
            l_sum += nums[i]
            if s == l_sum:
                return i

        return -1

