import collections
import sys
sys.setrecursionlimit(10**7+1)

N=int(sys.stdin.readline())
graph=collections.defaultdict(list)
in_degree=[0 for _ in range(N+1)]
for _ in range(N-1):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    in_degree[b]+=1
values=list(map(int,sys.stdin.readline().split()))
visited=[False for _ in range(N)]
root=0
for i in range(N):
    if in_degree[i]==0:
        root=i
        break

def dfs(node):
    tmp=values[node]
    visited[node]=True
    for next_node in graph[node]:
        if not visited[next_node]:
            v=dfs(next_node)
            if v>0:
                tmp+=v

    return tmp

print(dfs(root))