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

    return arr


# arr1 = [4, 7, 3, 1, 8, 5]
# print(selection_sort(arr1))
