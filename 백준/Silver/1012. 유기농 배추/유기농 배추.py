import sys
sys.setrecursionlimit(10**6)

t=int(input())
for _ in range(t):
    m,n,k=map(int,sys.stdin.readline().split())
    cabbages=[[0 for i in range(m)]for i in range(n)]
    need_cabbages=0
    for _ in range(k):
        x,y=map(int,sys.stdin.readline().split())
        cabbages[y][x]=1
    def dfs(x,y):
        cabbages[y][x]=0
        if x>0 and cabbages[y][x-1]==1:
            dfs(x-1,y)
        if x<m-1 and cabbages[y][x+1]==1:
            dfs(x+1,y)
        if y>0 and cabbages[y-1][x]==1:
            dfs(x,y-1)
        if y<n-1 and cabbages[y+1][x]==1:
            dfs(x,y+1)
    for y in range(n):
        for x in range(m):
            if cabbages[y][x]==1:
                need_cabbages+=1
                dfs(x,y)
    print(need_cabbages)