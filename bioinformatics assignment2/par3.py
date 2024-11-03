
def three_way_partition(n, A):
   
    pivot = A[0]
    less = 0          
    equal = 0         
    greater = n - 1   
    
    while equal <= greater:
        if A[equal] < pivot:
            A[less], A[equal] = A[equal], A[less]
            less += 1
            equal += 1
        elif A[equal] == pivot:
            equal += 1
        else:  
            A[equal], A[greater] = A[greater], A[equal]
            greater -= 1

   
    return A


n = 9
A = [4, 5, 6, 4, 1, 2, 5, 7, 4]
B = three_way_partition(n, A)


print(' '.join(map(str, B)))
