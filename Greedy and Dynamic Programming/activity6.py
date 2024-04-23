memo = {}
coins = [5, 1, 2, 10, 6, 2]

def F(i):
    
    if i >= len(coins):
        return 0
    if i in memo:
        return memo[i]

    best = max(F(i+2) + coins[i], F(i+1))
    memo[i] = best
    return memo[i]

print(F(0)) #output: 17 -> (5+10+2)
