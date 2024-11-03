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

def build_max_heap(A):
    n = len(A)
    for i in range(n // 2, 0, -1):
        heapify(A, n, i)

    return A


n = 5
A = [1, 3, 5, 7, 2]
B = build_max_heap(A)


print(' '.join(map(str, B)))
