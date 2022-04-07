import math


class Solution(object):
    def merge_sorted_GAP(self, arr1, arr2):
        m = len(arr1)
        n = len(arr2)
        gap = math.ceil((m + n) / 2)
        p1 = 0
        p2 = gap
        while gap != 0:
            while p2 < (m + n):
                if p1 < m and p2 < m:
                    if arr1[p1] > arr1[p2]:
                        temp = arr1[p1]
                        arr1[p1] = arr1[p2]
                        arr1[p2] = temp
                elif p1 < m and p2 >= m:
                    if arr1[p1] > arr2[(p2 % m)]:
                        temp = arr1[p1]
                        arr1[p1] = arr2[(p2 % m)]
                        arr2[(p2 % m)] = temp
                elif p1 >= m and p2 >= m:
                    if arr2[(p1 % m)] > arr2[(p2 % m)]:
                        temp = arr2[(p1 % m)]
                        arr2[(p1 % m)] = arr2[(p2 % m)]
                        arr2[(p2 % m)] = temp
                p1 += 1
                p2 += 1
            gap //= 2
            p1 = 0
            p2 = gap
        print(arr1)
        print(arr2)

Solution().merge_sorted_GAP([1,4,7,8,10], [2,3,9])
