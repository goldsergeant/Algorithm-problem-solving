import sys

N, X = map(int, sys.stdin.readline().split())
pipes = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0 for _ in range(X + 1)] for _ in range(N + 1)]
dp[0][0] = 1
for i in range(1, N + 1):
    for j in range(X + 1):
        for k in range(pipes[i-1][1] + 1):
            pre_length = j-pipes[i-1][0]*k
            if pre_length >= 0:
                dp[i][j] += dp[i-1][pre_length]

print(dp[-1][X])
