class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ma = 0
        j = -1
        for i in range(len(nums)):
            if nums[i] == 1:
                if i - j > ma:
                    ma = i - j
            else:
                j = max(i, j)
        return ma
