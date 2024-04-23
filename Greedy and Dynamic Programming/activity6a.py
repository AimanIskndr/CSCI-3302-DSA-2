memo = {}
coins = [5, 1, 2, 10, 6, 2]

def F(n):
    
    if n < 0:
        return 0
    if n in memo:
        return memo[n]
    
    best = max(F(n-3) + coins[n], F(n-2), F(n-1))
    return best

print(F(len(coins) - 1)) #output : 15
