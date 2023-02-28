import collections
import sys

global order
order=1
n,m,r=map(int,sys.stdin.readline().split())
graph=collections.defaultdict(list)
visit_order=dict()
for _ in range(m):
    u,v=map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1,n+1):
    graph[i].sort(reverse=True)

queue=collections.deque([r])
visited=[False for i in range(n+1)]
visited[r]=True
while queue:
    u=queue.pop()
    visit_order[u]=order
    order+=1
    for v in graph[u]:
        if not visited[v]:
            visited[v]=True
            queue.appendleft(v)

for i in range(1,n+1):
    print(visit_order.get(i,0))
