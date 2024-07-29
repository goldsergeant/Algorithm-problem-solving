import sys

def solution(m, n, puddles):
    answer = 0
    puddles_set=set()
    mod=1000000007
    dp=[[-1 for _ in range(n+1)] for _ in range(m+1)]
    for x,y in puddles:
        puddles_set.add((x,y))
        
    def dfs(x,y):
        if x==m and y==n:
            return 1
        if dp[x][y]!=-1:
            return dp[x][y]
        
        dp[x][y]=0
        for dx,dy in (1,0),(0,1):
            nx,ny=x+dx,y+dy
            if nx>m or ny>n or (nx,ny) in puddles_set:
                continue
            dp[x][y]= (dp[x][y]+dfs(nx,ny))%mod
        return dp[x][y]
    
    return dfs(1,1)