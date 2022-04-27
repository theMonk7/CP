# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        peak_point = self.__findPeak(mountain_arr)

        ans = self.__bin_search(mountain_arr, target, 0, peak_point, True)
        if ans == -1:
            ans = self.__bin_search(mountain_arr, target, peak_point + 1, mountain_arr.length() - 1, False)
        return ans

    def __findPeak(self, mountainArray: 'MountainArray') -> int:
        l = 0
        h = mountainArray.length() - 1

        while l < h:
            m = (l + h) // 2
            m_el = mountainArray.get(m)
            m_el_next = mountainArray.get(m + 1)
            if m_el < m_el_next:
                l = m + 1
            else:
                h = m

        return l

    def __bin_search(self, mountainArray: 'MountainArray', target: int, l: int, h: int, asc: bool) -> int:
        while l <= h:
            m = (l + h) // 2
            m_el = mountainArray.get(m)
            if m_el == target:
                return m
            elif m_el < target:
                if asc:
                    l = m + 1
                else:
                    h = m - 1
            else:
                if asc:
                    h = m - 1
                else:
                    l = m + 1

        return -1
