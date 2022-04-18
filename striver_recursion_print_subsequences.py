def print_subsequences(s, n, temp_arr, i, res_arr):
    if i >= n:
        res_arr.append(temp_arr)
        return
    temp_arr.append(s[i])
    print_subsequences(s, n, temp_arr.copy(), i + 1, res_arr)
    temp_arr.pop()
    print_subsequences(s, n, temp_arr.copy(), i + 1, res_arr)


s = "abcc"
n = len(s)
res = []
print_subsequences(s, n, [], 0, res)
res = list(map(list, set(map(tuple, res))))
res.sort()
print(res)
