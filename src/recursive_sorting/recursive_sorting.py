# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    # for i in range(0, len(arrA)):
    #     merged_arr[i] = arrA[i]
    # for i in range(0, len(arrB)):
    #     merged_arr[i + len(arrA)] = arrB[i]
    i = 0
    j = 0
    k = 0
    while i < len(arrA) and j < len(arrB):
        if arrA[i] < arrB[j]:
            merged_arr[k] = arrA[i]
            i += 1
        else:
            merged_arr[k] = arrB[j]
            j += 1
        k += 1

    while i < len(arrA):
        merged_arr[k] = arrA[i]
        i += 1
        k += 1

    while j < len(arrB):
        merged_arr[k] = arrB[j]
        j += 1
        k += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) <= 1:
        return arr

    midpoint = len(arr) // 2
    left_arr = arr[:midpoint]
    right_arr = arr[midpoint:]

    if len(left_arr) > 1:
        left_arr = merge_sort(left_arr)

    if len(right_arr) > 1:
        right_arr = merge_sort(right_arr)

    temp_arr = merge(left_arr, right_arr)
    # print(temp_arr)
    arr = temp_arr

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr


arr3 = [3, 9, 7, 4, 6, 1, 12, 2, 25]

print(merge_sort(arr3))
