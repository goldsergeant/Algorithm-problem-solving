import sys


N,M=map(int,sys.stdin.readline().split())
satisfied_score=[[*map(int,sys.stdin.readline().split())] for _ in range(M)]
dp=[[0 for _ in range(N)] for _ in range(M)]

for r in range(M):
    dp[r][0]=satisfied_score[r][0]

for j in range(1,N):
    for i in range(M):
        for k in range(M):
            if i==k:
                dp[i][j]=max(dp[i][j],dp[k][j-1]+satisfied_score[i][j]//2)
            else:
                dp[i][j]=max(dp[i][j],dp[k][j-1]+satisfied_score[i][j])

answer=0
for i in range(M):
    answer=max(answer,dp[i][-1])
print(answer)