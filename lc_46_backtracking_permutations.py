class Solution(object):

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.bt_p(nums, len(nums), [], res)
        return res

    def bt_p(self, nums, n, temp, res):
        if len(temp) == n:
            res.append(temp)
            return
        for k in range(0, n):
            if nums[k] in temp: continue
            temp.append(nums[k])
            self.bt_p(nums, n, temp[:], res)
            temp.pop()
    res2 = []
    def swap_permute(self,nums,n,i):
        if i == n:
            self.res2.append(nums)
            return
        for k in range(i,n):
            nums[k],nums[i] = nums[i], nums[k]
            self.swap_permute(nums[:],n,i+1)
            nums[k], nums[i] = nums[i], nums[k]


# print(Solution().permute([1,2,3]))
Solution().swap_permute([1,2,3],3,0,)
print(Solution().res2)