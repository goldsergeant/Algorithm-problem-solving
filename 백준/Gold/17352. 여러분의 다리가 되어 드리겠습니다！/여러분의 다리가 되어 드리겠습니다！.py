import collections
import sys
sys.setrecursionlimit(1000000)

def dfs(node):
    visited[node]=True
    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node)

N=int(sys.stdin.readline())
graph=collections.defaultdict(list)
for _ in range(N-2):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited=[False]*(N+1)

for i in range(1,N+1):
    if not visited[i]:
        dfs(i)
        print(i,end=' ')
