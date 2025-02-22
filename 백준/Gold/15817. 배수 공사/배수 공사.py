import sys

N, X = map(int, sys.stdin.readline().split())
pipes = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp=[[0 for _ in range(X+1)] for _ in range(N+1)]
dp[0][0]=1
for i in range(N):
    for j in range(X+1):
        for k in range(pipes[i][1]+1):
            next_length=j+pipes[i][0]*k
            if next_length<=X:
                dp[i+1][next_length]+=dp[i][j]

print(dp[-1][X])