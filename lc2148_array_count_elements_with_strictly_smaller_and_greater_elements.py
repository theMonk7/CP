class Solution:
    def countElements(self, nums: List[int]) -> int:
        m = min(nums)
        M = max(nums)
        cnt = 0
        for el in nums:
            if m < el < M:
                cnt +=1
        return cnt