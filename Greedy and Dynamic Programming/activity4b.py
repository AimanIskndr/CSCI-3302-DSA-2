INF = 10e9 + 7
coins = [6, 5, 1]
memo = {}

def min_num_coins(x):
    if x < 0:
        return INF
    if x == 0:
        return 0
    if x in memo:
        return memo[x]

    best = INF
    for c in coins:
        best = min(best, min_num_coins(x - c) + 1)

    memo[x] = best
    return best

x = int(input())
cnt = min_num_coins(x)
print(cnt)
