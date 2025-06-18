def merge_sort(arr: list) -> list:
    len = arr.__len__()
    if len <= 1:
        return arr
    idx = int(len/2)
    left = merge_sort(arr[0:idx])
    right = merge_sort(arr[idx: len])
    llen = left.__len__()
    rlen = right.__len__()
    if rlen == 0:
        return left
    if llen == 0:
        return right
    l = 0
    r = 0
    out = []
    
    while l < llen and r < rlen:
        if left[l] < right[r]:
            out.append(left[l])
            l += 1
        else:
            out.append(right[r])
            r += 1
    if l == llen:
        out = out + right[r:rlen]
    else:
        out = out + left[l:llen]
    # print(out)
    return out


unsorted_arr = [23, 71, 84, 62, 19, 24,  1, 81, 89, 56, 25, 99, 29, 51, 10, 16, 38, 49, 17, 52, 58, 48, 69, 28, 61, 45,  3,  6, 12, 42, 74, 93, 46, 80, 55, 50, 18, 41, 53, 72, 87, 36, 60, 15,  4, 30, 27, 94,  2, 98, 37, 64, 86, 43, 26, 59, 97, 75,  8, 35, 34, 78, 83, 54, 39, 68, 96, 88, 44, 95,  7, 79, 14, 40, 63,  9, 85, 11, 82, 76, 13, 31, 20,  5, 77, 100, 91, 90, 92, 66, 33, 32, 73, 22, 21, 70, 65, 67, 57, 47]

print(merge_sort(unsorted_arr))

