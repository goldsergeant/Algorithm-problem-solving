import sys

mod_num=1000000000
n,k=map(int,sys.stdin.readline().split())
dp=[[0]*(n+1) for _ in range(k+1)]
dp[1][1]=1
for i in range(1,k+1):
    for j in range(1,n+1):
        if j==1:
            dp[i][j]=i
            continue
        dp[i][j]=(dp[i-1][j]+dp[i][j-1])%mod_num

print(dp[k][n]%mod_num)