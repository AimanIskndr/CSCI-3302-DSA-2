INF = 10e9 + 7
coins = [6, 5, 1]
memo = {}

def solve(x):
    if x < 0:
        return INF
    if x == 0:
        return 0
    if x in memo:
        return memo[x]


    best = INF
    for c in coins:
        best = min(best, solve(x - c) + 1)

    memo[x] = best
    return best


change = int(input())
cnt = solve(change)
print(cnt)
# input: 76 | output: 13
