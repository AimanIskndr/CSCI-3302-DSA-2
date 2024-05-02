memo = {}
coins = [5, 1, 2, 10, 6, 2]

def F(i):
    if i >= len(coins):
        return []
    if i in memo:
        return memo[i]

    combination_with = [coins[i]] + F(i+2)
    combination_without = F(i+1)
    
    best_combination = combination_with if sum(combination_with) > sum(combination_without) else combination_without
    
    memo[i] = best_combination
    return memo[i]

print(F(0))
