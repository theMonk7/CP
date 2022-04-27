import math


class Recursion_Basics:

    def print_till_n_1(self, n: int) -> None:
        if n == 0:
            return
        self.print_till_n_1(n - 1)
        print(n)

    def factorial(self, n: int) -> int:
        if n == 1:
            return 1
        up = self.factorial(n - 1)
        return up * n

    def sum_of_digits(self, num: int) -> int:
        if num == 0:
            return 0
        return num % 10 + self.sum_of_digits(num // 10)

    def reverse_number(self, num: int) -> int:
        if num // 10 == 0:
            return num
        last = num % 10
        up = self.reverse_number(num // 10)
        return int(last * pow(10, math.log10(num) // 1) + up)

    def count_zeros(self, num: int, counter: int) -> int:
        if num == 0:
            return counter
        if num % 10 == 0:
            counter += 1
        return self.count_zeros(num // 10, counter)

    def is_array_sorted(self, arr, i) -> bool:
        if i == len(arr) - 1:
            return True
        return arr[i] <= arr[i + 1] and self.is_array_sorted(arr, i + 1)

    def linear_search(self, arr: list[int], index: int, target: int) -> int:
        if index == len(arr):
            return -1
        if arr[index] == target:
            return index
        else:
            return self.linear_search(arr, index + 1, target)

    def selection_sort(self, nums: list[int], index: int):
        if index == 0:
            return
        max_index: int = 0
        for i in range(0, index):
            if nums[i] > nums[max_index]:
                max_index = i
        nums[index - 1], nums[max_index] = nums[max_index], nums[index - 1]
        self.selection_sort(nums, index - 1)

    def string_filter(self, s1: str, filt: str) -> str:
        if len(s1) == 0:
            return ""
        pro = ""
        if s1[0] != filt:
            pro += s1[0]
        return pro + self.string_filter(s1[1:], filt)

    def skip_string(self, s1: str, filt: str, filt_len: int) -> str:
        if len(s1) == 0:
            return ""
        if s1[:filt_len] == filt:
            return self.skip_string(s1[5:], filt, filt_len)
        else:
            return s1[0] + self.skip_string(s1[1:], filt, filt_len)


recursion = Recursion_Basics()
# recursion.print_till_n_1(6)
# print(recursion.factorial(6))
# print(recursion.sum_of_digits(12345))
# print(recursion.reverse_number(123))
# print(recursion.count_zeros(1201002100, 0))
# print(recursion.is_array_sorted([1, 2, 3, 3, 4, 5, 6, 10, 11, 10], 0))
# print(recursion.linear_search([2, 3, 4, 1, 2, 3, 45, 324, 211, 56], 0, 56))
arr = [2, 4, 2, 1, 9, 3, 0]
# recursion.selection_sort(arr, len(arr))
# print(arr)

# print(recursion.string_filter("abcdfdada", "a"))
print(recursion.skip_string("This is apple and apple is very very appley", "apple", 5))
