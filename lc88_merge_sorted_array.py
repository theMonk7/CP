import math


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        last, ar1, ar2 = len(nums1) - 1, m - 1, n - 1
        while last >= 0 and ar2 >= 0:

            if nums1[ar1] > nums2[ar2] and ar1 >= 0:
                nums1[last] = nums1[ar1]
                ar1 -= 1
            else:
                nums1[last] = nums2[ar2]
                ar2 -= 1
            last -= 1