class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        f = 0
        q = -1
        for i in range(len(nums)):
            q += 1
            if nums[i] != nums[f]:
                if q == 1:
                    return nums[f]
                else:
                    q = 0
                    f = i
        return nums[f]



