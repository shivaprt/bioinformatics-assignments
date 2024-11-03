def heapify(A, n, i):
    largest = i      
    left = 2 * i    
    right = 2 * i + 1
   
    if left <= n and A[left - 1] > A[largest - 1]:
        largest = left

  
    if right <= n and A[right - 1] > A[largest - 1]:
        largest = right

    
    if largest != i:
        A[i - 1], A[largest - 1] = A[largest - 1], A[i - 1] 

     
        heapify(A, n, largest)

def heap_sort(A):
    n = len(A)
    
    
    for i in range(n // 2, 0, -1):
        heapify(A, n, i)

   
    for i in range(n, 1, -1):
        
        A[i - 1], A[0] = A[0], A[i - 1] 

        
        heapify(A, i - 1, 1)

    return A


n = 9
A = [2, 6, 7, 1, 3, 5, 4, 8, 9]
sorted_A = heap_sort(A)

print(' '.join(map(str, sorted_A)))
