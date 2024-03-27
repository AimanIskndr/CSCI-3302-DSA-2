def bubble_sort(arr):
    n = len(arr) - 1
    for i in range(n):
        for j in range(n-i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
            print(str(i) +", " + str(j) + ": " + str(arr))

arr = [2, 7, 9, 1, 5, 4, 6, 8, 3]
bubble_sort(arr)
