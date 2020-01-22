def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    for i in range(elements):
        if arrA == []:
            merged_arr[i] = arrB.pop(0)
        elif arrB == []:
            merged_arr[i] = arrA.pop(0)
        elif arrA[0] <= arrB[0]:
            merged_arr[i] = arrA.pop(0)
        elif arrB[0] <= arrA[0]:
            merged_arr[i] = arrB.pop(0)
    return merged_arr


def merge_sort(arr):
    if len(arr) > 1:
        split_point = round(len(arr)/2)

        left_side = arr[0:split_point]
        right_side = arr[split_point:len(arr)]

        return(merge(merge_sort(left_side), merge_sort(right_side)))

    else:
        return(arr)
