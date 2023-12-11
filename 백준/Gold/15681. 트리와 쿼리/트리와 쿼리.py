import collections
import sys
sys.setrecursionlimit(1000000)

N,R,Q=map(int,sys.stdin.readline().split())
tree=collections.defaultdict(list)
visited=[-1]*(N+1)
for _ in range(N-1):
    u,v=map(int,sys.stdin.readline().split())
    tree[u].append(v)
    tree[v].append(u)

def dfs(node):
    visited[node]=1
    for next_node in tree[node]:
        if visited[next_node]==-1:
            visited[node]+=dfs(next_node)
    return visited[node]

dfs(R)

for _ in range(Q):
    print(visited[int(sys.stdin.readline())])
