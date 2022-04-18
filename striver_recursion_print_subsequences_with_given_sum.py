def rec_subsequences_sum_k(arr, n, i, temp_arr, res, s):
    if i >= n:
        if s == 0:
            res.append(temp_arr)
        return
    temp_arr.append(arr[i])
    rec_subsequences_sum_k(arr, n, i + 1, temp_arr.copy(), res, s - arr[i])
    temp_arr.pop()
    rec_subsequences_sum_k(arr, n, i + 1, temp_arr.copy(), res, s)


def rec_any_1_subsequence_sum_k(arr, n, i, temp_arr, res, s):
    if i >= n:
        if s == 0:
            res.append(temp_arr)
            return True
        else:
            return False
    temp_arr.append(arr[i])
    if rec_any_1_subsequence_sum_k(arr, n, i + 1, temp_arr.copy(), res, s - arr[i]): return True
    temp_arr.pop()
    if rec_any_1_subsequence_sum_k(arr, n, i + 1, temp_arr.copy(), res, s): return True
    return False


a = [1, 2, 3, 5, 4, 6, 9]
su = 12
res = []
rec_subsequences_sum_k(a,len(a),0,[],res,su)
# rec_any_1_subsequence_sum_k(a, len(a), 0, [], res, su)
print(res)
