from itertools import permutations

def generate_permutations(n):
    """Generate all permutations of length n."""
    numbers = list(range(1, n + 1))
    perm_list = list(permutations(numbers))
    return perm_list
n = 3 
permutations_list = generate_permutations(n)
print(len(permutations_list))
for perm in permutations_list:
    print(" ".join(map(str, perm)))
