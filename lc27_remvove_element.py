class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0 or (len(nums) == 1 and nums[0] == val):
            return 0

        f, l = 0, len(nums) - 1

        while f != l:
            if nums[f] != val:
                f += 1
            else:
                nums[f] = nums[l]
                l -= 1

        return f if nums[f] == val else f + 1