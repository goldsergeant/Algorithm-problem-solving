import collections
import sys

def dfs(node,p_dinymite):

    child_dinymite = 0
    visited[node] = True
    for next_node,next_dinymite in graph[node]:
        if not visited[next_node]:
            visited[next_node] = True
            child_dinymite+=dfs(next_node,next_dinymite)

    return min(child_dinymite,p_dinymite) if child_dinymite!=0 else p_dinymite

T=int(sys.stdin.readline())
for _ in range(T):
    N,M=map(int,sys.stdin.readline().split())
    graph=collections.defaultdict(list)
    visited=[False for _ in range(N+1)]
    if N==1:
        print(0)
        continue
    for _ in range(M):
        a,b,d=map(int,sys.stdin.readline().split())
        graph[a].append((b,d))
        graph[b].append((a,d))

    print(dfs(1,sys.maxsize))