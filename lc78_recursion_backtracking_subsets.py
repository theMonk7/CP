class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.helper(nums, len(nums), 0, [], res)
        return res

    def helper(self, nums, n, i, temp, res):
        if i == n:
            res.append(temp)
            return
        temp.append(nums[i])
        self.helper(nums, n, i + 1, temp[:], res)
        temp.pop()
        self.helper(nums, n, i + 1, temp[:], res)

    def helper2_backtracking(self, nums, n, i, temp, res):
        res.append(temp)
        for k in range(i, n):
            temp.append(nums[k])
            self.helper(nums, n, k + 1, temp[:], res)
            temp.pop()