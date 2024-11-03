import random

def randomized_partition(A, low, high):
    
    pivot_index = random.randint(low, high)
   
    A[pivot_index], A[high] = A[high], A[pivot_index]
    pivot = A[high]
    
    
    i = low - 1
    for j in range(low, high):
        if A[j] < pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    
    
    A[i + 1], A[high] = A[high], A[i + 1]
    return i + 1

def randomized_select(A, low, high, k):
    if low == high: 
        return A[low]
    
    
    pivot_index = randomized_partition(A, low, high)
    
    
    left_size = pivot_index - low + 1
    
    if k == left_size: 
        return A[pivot_index]
    elif k < left_size: 
        return randomized_select(A, low, pivot_index - 1, k)
    else:  
        return randomized_select(A, pivot_index + 1, high, k - left_size)

def kth_smallest(A, k):
    n = len(A)
    return randomized_select(A, 0, n - 1, k)


n = 11
A = [2, 36, 5, 21, 8, 13, 11, 20, 5, 4, 1]
k = 8
result = kth_smallest(A, k)

print(result)
