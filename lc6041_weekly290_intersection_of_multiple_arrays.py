class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        ref = nums[0]
        temp = []
        for i in range(1,len(nums)):
            for j in range(len(ref)):
                if ref[j] in nums[i]:
                    temp.append(ref[j])
            ref = temp[:]
            temp = []
        return ref.sort()


print(Solution().intersection([[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]))