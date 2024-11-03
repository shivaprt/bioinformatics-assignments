def quick_sort(A):
    if len(A) <= 1:  
        return A
    
    pivot = A[-1]  
    left = []
    right = []

   
    for x in A[:-1]:  
        if x < pivot:
            left.append(x)
        else:
            right.append(x)

    
    return quick_sort(left) + [pivot] + quick_sort(right)


n = 7
A = [5, -2, 4, 7, 8, -10, 11]
sorted_A = quick_sort(A)


print(' '.join(map(str, sorted_A)))
