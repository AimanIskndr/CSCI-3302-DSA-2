memo = {}

def fib(n):
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

# test
for i in range(0, 10):
    print(fib(i), end=' ')
    # output: 0 1 1 2 3 5 8 13 21 34
