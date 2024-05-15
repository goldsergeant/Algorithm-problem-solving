import sys

N,T=map(int,sys.stdin.readline().split())
subjects=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
dp=[[0 for _ in range(T+1)] for _ in range(N+1)]
for i in range(1,N+1):
    time, score = subjects[i - 1]
    for j in range(T,-1,-1):
        if j-time>=0:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-time]+score)
        else:
            dp[i][j]=dp[i-1][j]

print(dp[N][T])