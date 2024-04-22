memo = {}
things = [[2, 20], [5, 30], [10, 50], [5, 10]]

def solve(w):
    
    if w in memo:
        return memo[w]
    
    best = 0
    for k, v in things:
        if w - k >= 0:
            best = max(best, solve(w-k) + v)

    memo[w] = best
    return memo[w]

print(solve(16)) # output: 160

