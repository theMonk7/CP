def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)

        i = j = p = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[p] = left[i]
                p += 1
                i += 1
            else:
                arr[p] = right[j]
                p += 1
                j += 1
        if i == len(left):
            while j < len(right):
                arr[p] = right[j]
                p += 1
                j += 1
        else:
            while i < len(left):
                arr[p] = left[i]
                p += 1
                i += 1

    return arr

print(merge_sort([5,3,6,5,2,1,0,-1,100,34]))



