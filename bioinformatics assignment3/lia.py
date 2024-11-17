from math import factorial
def combination(n, x):
    return factorial(n) // (factorial(x) * factorial(n - x))
def probability_of_AaBb(k, N):
    n = 2**k  
    p = 0.25
    total_prob = 0
    for x in range(0, N):
        prob_x = combination(n, x) * (p**x) * ((1-p)**(n-x))
        total_prob += prob_x
    at_least_N_prob = 1 - total_prob
    return round(at_least_N_prob, 6)  
k = 2
N = 1
result = probability_of_AaBb(k, N)
print(result)