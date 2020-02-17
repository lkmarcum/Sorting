# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # print(i)
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        temp_value = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp_value

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    while True:
        num_swaps = 0
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i + 1]:
                temp_value = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp_value
                num_swaps += 1

        if num_swaps == 0:
            break

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    if len(arr) == 0:
        return arr
    else:
        min = arr[0]
        max = 0

        for i in range(0, len(arr)):
            if arr[i] < min:
                min = arr[i]
            elif arr[i] > max:
                max = arr[i]

        if min < 0:
            return "Error, negative numbers not allowed in Count Sort"
        else:

            count_arr = [0 for i in range(0, max - min + 1)]
            for i in range(0, len(arr)):
                count_arr[arr[i] - min] += 1
            for i in range(1, len(count_arr)):
                count_arr[i] += count_arr[i - 1]
            temp_arr = [0 for i in range(0, len(arr))]
            for i in range(0, len(arr)):
                print(count_arr[arr[i] - min])
                temp_arr[count_arr[arr[i] - min] - 1] = arr[i]
                count_arr[arr[i] - min] -= 1
            arr = temp_arr
            return arr


arr1 = [14, 47, 23, -2, 8, 15]
print(count_sort(arr1))

#  1  2  3  4  5  6  7  8
# [0, 0, 0, 0, 0, 0, 0, 0]
