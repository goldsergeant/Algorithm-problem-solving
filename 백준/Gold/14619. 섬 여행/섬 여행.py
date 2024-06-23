import collections
import sys
from functools import cache
sys.setrecursionlimit(100000+1)

@cache
def dfs(node,cnt):
    if cnt==0:
        return height[node]

    tmp=sys.maxsize
    for next_node in graph[node]:
        tmp=min(tmp,dfs(next_node,cnt-1))

    return tmp

N,M=map(int,sys.stdin.readline().split())
height=[0]+[*map(int,sys.stdin.readline().split())]
graph=collections.defaultdict(list)
for _ in range(M):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

T=int(sys.stdin.readline())
for _ in range(T):
    a,k=map(int,sys.stdin.readline().split())
    print(dfs(a,k) if dfs(a,k)!=sys.maxsize else -1)