class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        hm = {}
        arr = sorted(nums)
        cnt = 0
        res = []
        for i in range(len(arr)):
            if i == 0:
                hm[arr[i]] = 0

            elif arr[i] != arr[i - 1]:
                hm[arr[i]] = cnt

            cnt += 1
        for el in nums:
            res.append(hm[el])
        return res