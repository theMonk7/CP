class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        for r in range(1, len(nums)):
            if nums[l] != nums[r]:
                l += 1
                nums[l] = nums[r]

        print(nums)

        return l + 1


print(Solution().removeDuplicates([1,1,1,1,3,3,3,4,5]))


a = [2342,43,34,34,2,3,4,3,2,2,3,4,2]
a.remove(2)
print(a)