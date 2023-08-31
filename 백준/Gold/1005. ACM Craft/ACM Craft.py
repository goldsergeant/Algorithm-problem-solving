import collections
import sys

sys.setrecursionlimit(100000)

t=int(input())
def dfs(num):
    if dp[num]==-1:
        dp[num]=max([dfs(c) for c in graph[num]],default=0)+d[num]
    return dp[num]


for _ in range(t):
    n,k=map(int,input().split())
    d=[0]+list(map(int,input().split()))
    graph=collections.defaultdict(list)
    for _ in range(k):
        x,y=map(int,input().split())
        graph[y].append(x)

    dp=[-1 for _ in range(n+1)]
    print(dfs(int(input())))

