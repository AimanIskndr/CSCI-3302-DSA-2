def merge_sort(arr):
    
    if(len(arr) > 1):
        
        mid = len(arr)//2
        left_sub_arr = arr[:mid]
        right_sub_arr = arr[mid:]
        
        merge_sort(left_sub_arr)
        merge_sort(right_sub_arr)
        
        i = j = k = 0
        
        while i < len(left_sub_arr) and j < len(right_sub_arr):
            if left_sub_arr[i] < right_sub_arr[j]:
                arr[k] = left_sub_arr[i]
                i += 1
            else:
                arr[k] = right_sub_arr[j]
                j += 1
            k += 1
            
        while i < len(left_sub_arr):
            arr[k] = left_sub_arr[i]
            i += 1
            k += 1
            
        while j < len(right_sub_arr):
            arr[k] = right_sub_arr[j]
            j += 1
            k += 1
        
        print(arr)
        return arr
    
arr = [2, 7, 9, 1, 5, 4, 6, 8, 3]
merge_sort(arr)