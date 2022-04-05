class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mp = {}
        for i in range(len(nums)):
            if mp.__contains__(target - nums[i]):
                print(mp)
                return [i, mp[target - nums[i]]]
            else:
                mp[nums[i]] = i



print(Solution().twoSum([3,3,], 6))

