def partition_array(n, A):
    
    pivot = A[0]
    j = 1

    
    for i in range(1, n):
        if A[i] <= pivot:
            
            A[i], A[j] = A[j], A[i]
            j += 1
    
    
    A[0], A[j - 1] = A[j - 1], A[0]

    return A


n = 9
A = [7, 2, 5, 6, 1, 3, 9, 4, 8]
B = partition_array(n, A)


print(' '.join(map(str, B)))







