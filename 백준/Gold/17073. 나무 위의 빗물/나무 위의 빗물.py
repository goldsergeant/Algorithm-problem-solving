import collections
import sys

N,W=map(int,sys.stdin.readline().split())
tree=collections.defaultdict(list)
out_degree=[0 for _ in range(N+1)]
for _ in range(N-1):
    u,v=map(int,sys.stdin.readline().split())
    tree[u].append(v)
    tree[v].append(u)

visited=[False for _ in range(N+1)]
q=collections.deque([1])
visited[1]=True
while q:
    node=q.popleft()
    for next_node in tree[node]:
        if not visited[next_node]:
            visited[next_node]=True
            q.append(next_node)
            out_degree[node]+=1

print(W/out_degree[1:].count(0))