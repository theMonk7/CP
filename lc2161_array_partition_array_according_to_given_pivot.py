class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:

        # left = []
        # right = []
        # pivots = []
        # for e in nums:
        #     if e < pivot:
        #         left.append(e)
        #     elif e > pivot:
        #         right.append(e)
        #     else:
        #         pivots.append(e)
        # return left+pivots+right
        sol = []
        for e in nums:
            if e < pivot:
                sol.append(e)
        for e in nums:
            if e == pivot:
                sol.append(e)
        for e in nums:
            if e > pivot:
                sol.append(e)
        return sol