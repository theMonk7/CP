class Solution:
    def findPeakElement(self, arr: List[int]) -> int:
        l = 0
        h = len(arr) - 1

        while l < h:
            m = (h + l) // 2
            if arr[m] > arr[m + 1]:
                h = m
            else:
                l = m + 1
        return l