import sys

N,K=map(int,sys.stdin.readline().split())
subjects=[(0,0)]+[tuple(map(int,sys.stdin.readline().split())) for _ in range(K)]
dp=[[0 for _ in range(N+1)] for _ in range(K+1)]

for i in range(1,K+1):
    for j in range(N,0,-1):
        if j-subjects[i][1]>=0:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-subjects[i][1]]+subjects[i][0])
        else:
            dp[i][j]=dp[i-1][j]

print(dp[K][N])