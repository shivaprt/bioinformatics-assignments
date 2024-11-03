import heapq
def k_smallest_elements_heap(A, k):
    
    return heapq.nsmallest(k, A)
n = 10
A = [4, -6, 7, 8, -9, 100, 12, 13, 56, 17]
k = 3
result = k_smallest_elements_heap(A, k)
print(' '.join(map(str, result)))
