def array_rev(arr, n):
    if n == 1:
        return arr
    temp = arr[0]
    arr1 = array_rev(arr[1:], n - 1)
    arr1.append(temp)
    return arr1


def array_rec_2_ptr(arr, l, r):
    if l == r:
        return arr
    arr[l], arr[r] = arr[r], arr[l]
    return array_rec_2_ptr(arr, l + 1, r - 1)


def array_rec_1_ptr(arr, i, n):
    if i > n // 2:
        return arr
    arr[i], arr[n - i - 1] = arr[n-i-1], arr[i]
    return array_rec_1_ptr(arr, i + 1, n)


# print(array_rev([1,2,3,4,5],5))
# print(array_rec_2_ptr([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 9 - 1))
print(array_rec_1_ptr([1, 2, 3, 4, 5, 6, 7], 0, 7))
