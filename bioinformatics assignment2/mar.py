def merge_sorted_arrays(A, B):
    
    i, j = 0, 0
    C = []  
    
   
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    
    
    C.extend(A[i:])
    C.extend(B[j:])
    
    return C


n = 4
A = [2, 4, 10, 18]
m = 3
B = [-5, 11, 12]


C = merge_sorted_arrays(A, B)
print(" ".join(map(str, C)))
