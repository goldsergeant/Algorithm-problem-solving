import sys

MOD_NUM=1000000003

N=int(sys.stdin.readline())
K=int(sys.stdin.readline())

dp=[[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(2,N+1):
    dp[i][0]=1
    dp[i][1]=i
    for j in range(2,K+1):
        dp[i][j]=(dp[i-1][j]+dp[i-2][j-1])%MOD_NUM

print(dp[N][K])