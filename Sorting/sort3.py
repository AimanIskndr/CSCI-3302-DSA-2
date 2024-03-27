def insertion_sort(arr):
    n = len(arr)
    for i in range(0, n):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
        print(str(i) + ": " + str(arr))
    
    return
    
arr = [2, 7, 9, 1, 5, 4, 6, 8, 3]
insertion_sort(arr)
