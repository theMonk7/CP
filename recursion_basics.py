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

    def uniquePathsInAMatrixDownRight(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        return self.uniquePathsInAMatrixDownRight(m - 1, n) + self.uniquePathsInAMatrixDownRight(m, n - 1)

    def printPathInMatrixTraversalRightDown(self, m: int, n: int, choices: list[str], path: str):
        if m == 1 and n == 1:
            print(path)
            return

        if m > 1:
            self.printPathInMatrixTraversalRightDown(m - 1, n, choices, path + "D")
        if n > 1:
            self.printPathInMatrixTraversalRightDown(m, n - 1, choices, path + "R")
        if n > 1 and m > 1:
            self.printPathInMatrixTraversalRightDown(m - 1, n - 1, choices, path + "d")

    def traversing_matrix_with_obstacles(self, board: list[list[bool]], r: int, c: int, path: str):
        if r == 1 and c == 1:
            print(path)
            return
        if r > 1 and board[len(board) - r][len(board[0]) - c]:
            self.traversing_matrix_with_obstacles(board, r - 1, c, path + "D")
        if c > 1 and board[len(board) - r][len(board[0]) - c]:
            self.traversing_matrix_with_obstacles(board, r, c - 1, path + "R")

    def traversing_matrix_with_obstacles_all_directions(self, board: list[list[bool]], r: int, c: int, path: str):

        if r == len(board) - 1 and c == len(board[0]) - 1:
            print(path)
            return
        if not board[r][c]:
            return
        board[r][c] = False
        if r < len(board) - 1:
            self.traversing_matrix_with_obstacles_all_directions([row[:] for row in board], r + 1, c, path + "D")
        if c < len(board[0]) - 1:
            self.traversing_matrix_with_obstacles_all_directions([row[:] for row in board], r, c + 1, path + "R")
        if r > 0:
            self.traversing_matrix_with_obstacles_all_directions([row[:] for row in board], r - 1, c, path + "U")
        if c > 0:
            self.traversing_matrix_with_obstacles_all_directions([row[:] for row in board], r, c - 1, path + "L")
        board[r][c] = True


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
# print(recursion.skip_string("This is apple and apple is very very appley", "apple", 5))
# recursion.printPathInMatrixTraversalRightDown(3, 3, ["D", "R"], "")

board = [
    [True, True, True],
    [True, False, True],
    [True, True, True]
]


# recursion.traversing_matrix_with_obstacles(board, len(board), len(board[0]), "")
# recursion.traversing_matrix_with_obstacles_all_directions(board, 0, 0, "")


# Coding Ninjas Recursion
# pip => 3.14p
# ppi

def func(s: list[str]):
    if len(s) <= 0:
        return ""
    if len(s) == 1:
        return s[0]
    elif s[0] == "p" and s[1] == "i":
        p = func(s[2:])
        return "3.14" + p
    else:
        p = func(s[1:])
        return s[0] + p


def removeX(s: str):
    return "".join(__helper(list(s), 0))


import math


def __helper(s: list[str], ind: int):
    if ind >= len(s):
        return s
    if s[ind] == "x":
        s[ind] = ""
    return __helper(s, ind + 1)


def string_to_int(s: str, ind: int, cnt: int, f=False):
    if ind == len(s) - 1:
        return ord(s[ind]) - ord("0")
    k = s[ind]
    if k == "0" and not f:
        return string_to_int(s, ind + 1, f)
    else:
        f = True
        p = ord(k) - ord("0")
        temp = string_to_int(s, ind + 1, cnt + 1, f)

        return p * pow(10, cnt) + temp


def maximise():
    m = -100
    a = b = 0
    mi = 10000000000000
    for x in range(0, 10):
        for y in range(0, 6):
            if 137 * x + 351 * y <= 1221 and 2000 * x + 5000 * y >= m and 137 * x + 351 * y <= mi:
                a = x
                b = y
                m = 2000 * x + 5000 * y
                print(a, b, m, 137 * x + 351 * y)
    print(a, b, m)


# Driver code
if __name__ == "__main__":
    string = list("pippipi")

    # Function call
    # print(func(string))
    # print(removeX("jhjxh"))

    # print(string_to_int("123", 0,0))
    maximise()


def changeTree(root):
    # Write your code here.
    if root is None:
        return
    r = l = 0
    if root.left:
        l = root.left.data
    if root.right:
        r = root.right.data
    if root.data > r + l:
        if root.left:
            root.left.data = root.data
        if root.right:
            root.right.data = root.data
    changeTree(root.left)
    changeTree(root.right)
    if root.left or root.right:
        l = r = 0
        if root.left:
            l = root.left.data
        if root.right:
            r = root.right.data
        root.data = l + r
