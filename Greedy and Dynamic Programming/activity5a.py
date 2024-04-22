memo = {}

def F(n):
    if n <= 0:
        return 0
    if n <= 3:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = F(n-2) + F(n-3) + F(n-4)
    return memo[n]

# test
for i in range(0, 11):
    print(F(i), end=' ')
    # output: 0 1 1 1 2 3 4 6 9 13 19
