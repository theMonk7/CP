class BinarySearch:

    def bin_search(self, arr: list[int], val: int) -> int:
        l = 0
        h = len(arr) - 1

        while l <= h:
            m = l + (h - l) // 2
            if arr[m] == val:
                return m
            elif val > arr[m]:
                l = m + 1
            else:
                h = m - 1
        return -1

    def ceil_of_element(self, arr: list[int], val: int) -> int:
        l = 0
        h = len(arr) - 1
        while l <= h:
            m = l + (h - l) // 2
            if arr[m] == val:
                return m
            elif val > arr[m]:
                l = m + 1
            else:
                h = m - 1
        return l

    def floor_of_element(self, arr: list[int], val: int) -> int:
        l = 0
        h = len(arr) - 1
        while l <= h:
            m = l + (h - l) // 2
            if arr[m] == val:
                return m
            elif val > arr[m]:
                l = m + 1
            else:
                h = m - 1
        return h


b_s = BinarySearch()
arr = [1, 3, 67, 89, 123, 166, 200]
# print(b_s.bin_search(arr, 100))
print(b_s.ceil_of_element(arr, 165))
print(b_s.floor_of_element(arr, 70))
