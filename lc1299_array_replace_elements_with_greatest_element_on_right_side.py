class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        g_el = -1
        o_el = -1
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] > g_el:
                g_el = arr[i]
            arr[i] = o_el
            o_el = g_el
        return arr
