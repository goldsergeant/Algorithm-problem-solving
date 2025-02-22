import sys

N, K = map(int, sys.stdin.readline().split())
caffeines = [0]+list(map(int, sys.stdin.readline().split()))
dp=[[sys.maxsize for _ in range(K+1)] for _ in range(N+1)] # 커피, 카페인

dp[0][0]=0
for i in range(1,N+1):
    for j in range(K+1):
        pre_caffeine=j-caffeines[i]
        if pre_caffeine>=0:
            dp[i][j]=min(dp[i-1][j],dp[i-1][pre_caffeine]+1)
        else:
            dp[i][j]=dp[i-1][j]

print(dp[-1][K] if dp[-1][K]<sys.maxsize else -1)