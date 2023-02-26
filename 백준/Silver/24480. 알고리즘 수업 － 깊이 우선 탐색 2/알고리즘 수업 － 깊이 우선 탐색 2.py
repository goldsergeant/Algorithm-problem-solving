import collections
import sys
sys.setrecursionlimit(10**8)

n,m,r=map(int,sys.stdin.readline().split())
graph=collections.defaultdict(list)
for _ in range(m):
    u,v=map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1,n+1):
    graph[i].sort(reverse=True)

visited=[False for i in range(n+1)]
visit_order=dict()
global order
order=1
def dfs(r):
    global order
    visited[r]=True
    visit_order[r]=order
    order+=1
    for next in graph[r]:
        if not visited[next]:
            dfs(next)
dfs(r)

for i in range(1,n+1):
    print(visit_order.get(i,0))