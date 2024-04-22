coins = [5, 1, 2, 10, 6, 2]

def pick_up(i):
    
    if i >= len(coins):
        return 0
    
    best = 0
    best = max(pick_up(i+2) + coins[i], pick_up(i+1))
    return best

print(pick_up(0)) #output: 17 -> (5+10+2)
