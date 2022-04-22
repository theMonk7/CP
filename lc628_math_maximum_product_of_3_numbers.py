class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        import math
        min1 = min2 = math.inf
        max1 = max2 = max3 = -math.inf

        for e in nums:
            if e < min1:
                min2 = min1
                min1 = e
            elif e >= min1 and e < min2:
                min2 = e
            if e > max1:
                max3 = max2
                max2 = max1
                max1 = e
            elif e > max2 and e <= max1:
                max3 = max2
                max2 = e
            elif e > max3 and e <= max2:
                max3 = e

        return max(max1 * max2 * max3, min1 * min2 * max1)

print(Solution().maximumProduct([1,2,3,4,-2,-100]))