# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        num = arr[i]
        for j in range(i+1, len(arr)):
            if num > arr[j]:
                num = arr[j]
                arr[i], arr[j] = arr[j], arr[i]
        print(arr)
    return(arr)


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    sort = 1
    while sort == 1:
        flips = 0
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                flips += 1
        if flips == 0:
            sort = 0
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
