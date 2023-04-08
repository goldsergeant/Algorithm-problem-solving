import sys

n = int(input())
costs = []
r, g, b = 0, 1, 2
for _ in range(n):
    costs.append(list(map(int, sys.stdin.readline().split())))

answer=sys.maxsize
for i in range(3):
    dp = [[sys.maxsize for _ in range(3)] for _ in range(n)]
    dp[0][i]=costs[0][i]
    for j in range(1,n):
        dp[j][r]=costs[j][r]+min(dp[j-1][g],dp[j-1][b])
        dp[j][g]=costs[j][g]+min(dp[j-1][r],dp[j-1][b])
        dp[j][b]=costs[j][b]+min(dp[j-1][r],dp[j-1][g])

    for k in range(3):
        if i!=k:
            answer=min(answer,dp[n-1][k])

print(answer)