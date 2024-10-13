import sys
from functools import cache

N=int(sys.stdin.readline())
coding_powers=[int(sys.stdin.readline()) for _ in range(N)]
dp=[[0 for _ in range(N)] for _ in range(N)]
winner=[[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    winner[i][i] = coding_powers[i]
    for j in range(i+1,N):
        winner[i][j] = max(winner[i][j-1], coding_powers[j])



for i in range(N-1,-1,-1):
    for j in range(i+1,N):
        tmp=sys.maxsize
        for k in range(i,j):
            tmp=min(tmp,dp[i][k]+dp[k+1][j]+abs(winner[i][k]-winner[k+1][j]))
        dp[i][j]=tmp

print(dp[0][N-1])