import sys
sys.setrecursionlimit(100000+1)

def dfs(a,b):
    if a==a2 and b==b2:
        return 0
    if dp[a][b]!=-1:
        return dp[a][b]

    dp[a][b]=sys.maxsize
    if a<a1: # 물통 채우는 단계
        dp[a][b]=min(dp[a][b],dfs(a1,b)+1)
    if b<b1:
        dp[a][b]=min(dp[a][b],dfs(a,b1)+1)

    if a>0: # 물통 버리는 단계
        dp[a][b]=min(dp[a][b],dfs(0,b)+1)
    if b>0:
        dp[a][b]=min(dp[a][b],dfs(a,0)+1)

    if b<b1: # 물통 옮기는 단계
        if a<=b1-b:
            dp[a][b]=min(dp[a][b],dfs(0,b+a)+1)
        else:
            dp[a][b]=min(dp[a][b],dfs(a-(b1-b),b1)+1)
    if a<a1:
        if b<=a1-a:
            dp[a][b]=min(dp[a][b],dfs(a+b,0)+1)
        else:
            dp[a][b]=min(dp[a][b],dfs(a1,b-(a1-a))+1)

    return dp[a][b]


a1,b1,a2,b2=map(int,sys.stdin.readline().split())
dp=[[-1 for _  in range(b1+1)] for _ in range(a1+1)]
print(dfs(0,0) if dfs(0,0)!=sys.maxsize else -1)