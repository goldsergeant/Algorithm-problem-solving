import collections
import sys

N=int(sys.stdin.readline())
graph=collections.defaultdict(list)
answer=sys.maxsize
for _ in range(N-1):
    a,b=map(int,sys.stdin.readline().split())
    graph[b].append(a)

def dfs(v,visited):
    visited[v]=True

    for w in graph[v]:
        if not visited[w]:
            dfs(w,visited)

for i in range(1,N):
    if graph[i]:
        visited=[False]*(N+1)
        dfs(i,visited)
        if all(visited[1:]):
            answer=min(answer,i)
print(answer if answer!=sys.maxsize else -1)