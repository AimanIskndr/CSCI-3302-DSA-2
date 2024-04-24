dp = [[0] * 17 for _ in range(5)]
things = [[0, 0], [2, 20], [5, 30], [10, 50], [5, 10]]

def K(W):
    n = len(things)
    for i in range(1, n):
        w, v = things[i]
        for j in range(W + 1):
            dp[i][j] = dp[i-1][j]
            if j >= w:
                dp[i][j] = max(dp[i-1][j-w] + v, dp[i][j])
    return dp[n-1][W]

print(K(16))
