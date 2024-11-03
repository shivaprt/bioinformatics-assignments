def insertion_sort_swaps(arr):
    swap_count = 0  
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
           
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            swap_count += 1  
            j -= 1  
    
    return swap_count


n = 6
arr = [6, 10, 4, 5, 1, 2]

print(insertion_sort_swaps(arr))  
