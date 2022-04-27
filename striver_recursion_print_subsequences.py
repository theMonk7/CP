# Recursive approach
def print_subsequences(s, n, temp_arr, i, res_arr):
    if i >= n:
        res_arr.append(temp_arr)
        return
    temp_arr.append(s[i])
    print_subsequences(s, n, temp_arr.copy(), i + 1, res_arr)
    temp_arr.pop()
    print_subsequences(s, n, temp_arr.copy(), i + 1, res_arr)


s = "1223"
n = len(s)
res = []
# print_subsequences(s, n, [], 0, res)
res = list(map(list, set(map(tuple, res))))
res.sort()


# print(res)


# Iterative-Recursive approach ~ BACKTRACKING
def subsets_iterative(nums):
    if len(nums) == 0:
        return [[]]
    el = nums.pop()
    smaller = subsets_iterative(nums[:])
    n = len(smaller)
    for i in range(n):
        p = smaller[i][:]
        p.append(el)
        smaller.append(p)
    return smaller


# print(subsets_iterative([1, 2, 3]))


# Backtracking Approach
res_bt = []


def subsets_backtracking(nums, temp, i, n):
    res_bt.append(temp)
    for k in range(i, n):
        temp.append(nums[k])
        subsets_backtracking(nums, temp[:], k + 1, n)
        temp.pop()


p = [1, 2, 3]
# subsets_backtracking(p, [], 0, len(p))
# print(res_bt)
