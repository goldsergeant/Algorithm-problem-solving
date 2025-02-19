import sys

N, K = map(int, sys.stdin.readline().split())
coins = list(int(sys.stdin.readline()) for _ in range(N))
dp = [[sys.maxsize for _ in range(K + 1)] for _ in range(N)]

dp[0][0] = 0
for j in range(1, K + 1):
    if coins[0] <= j:
        dp[0][j] = dp[0][j - coins[0]] + 1

for i in range(1, N):
    dp[i][0] = 0
    for j in range(1, K + 1):
        if j - coins[i] >= 0:
            dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - coins[i]] + 1,dp[i][j - coins[i]] + 1)
        else:
            dp[i][j] = dp[i - 1][j]


print(dp[N - 1][K] if dp[N-1][K]<sys.maxsize else -1)
