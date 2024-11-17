def mortal_fibonacci_rabbits(n, m):
    rabbits = [0] * m
    rabbits[0] = 1
    for month in range(1, n):
        newone = sum(rabbits[1:])
        rabbits = [newone] + rabbits[:-1]
    return sum(rabbits)
n = 6
m = 3
print(mortal_fibonacci_rabbits(n, m))