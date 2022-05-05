class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        neg = []
        pos = []
        for e in nums:
            if e > 0:
                pos.append(e)
            else:
                neg.append(e)
        n = 0
        p = 0
        nums.clear()
        for i in range(len(pos) + len(neg)):
            if i % 2 == 0:
                nums.append(pos[p])
                p += 1
            else:
                nums.append(neg[n])
                n += 1
        return nums

print(Solution().rearrangeArray([3,1,-2,-5,2,-4]))