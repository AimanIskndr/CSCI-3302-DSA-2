def find_min_id(arr, min_id):
    for i in range(min_id, len(arr)):
        if arr[i] < arr[min_id]:
            min_id = i
    return min_id

def selection_sort(arr):
    for i in range(0, len(arr)):
        j = find_min_id(arr, i)
        arr[i], arr[j] = arr[j], arr[i]
        print(str(i) + ": " + str(arr))
        
arr = [2, 7, 9, 1, 5, 4, 6, 8, 3]
selection_sort(arr)       

