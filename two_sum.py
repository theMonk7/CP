class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(len(nums)):
            if dict.__contains__(nums[i]):
                dict[nums[i]][0] += 1
            else:
                dict[nums[i]] = [1, i]

        for i in range(len(nums)):
            if dict.__contains__(target - nums[i]) and dict[target - nums[i]][1] != i:
                return [i, dict[target - nums[i]][1]]

print(Solution().twoSum([2,7,11,15], 9))

