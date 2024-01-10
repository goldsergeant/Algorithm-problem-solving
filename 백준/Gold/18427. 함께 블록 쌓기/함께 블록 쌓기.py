import sys

N,M,H=map(int,sys.stdin.readline().split())
MOD_NUM=10007
dp=[[0 for _ in range(1000+1)] for _ in range(N+1)]
blocks=[[0 for _ in range(M)]]
for i in range(1,N+1):
    blocks.append(list(map(int,sys.stdin.readline().split())))

dp[0][0]=1
for i in range(1,N+1):
    dp[i][0]=1
    for j in range(1,H+1):
        for block in blocks[i]:
            if j-block>=0:
                dp[i][j]=(dp[i][j]+dp[i-1][j-block])%MOD_NUM
        dp[i][j]=(dp[i][j]+dp[i-1][j])%MOD_NUM

print(dp[N][H])