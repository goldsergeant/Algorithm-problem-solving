import collections
import sys

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
def dfs(node):
    global order
    stack=collections.deque()
    stack.append(node)
    while stack:
        next_node=stack.pop()
        if not visited[next_node]:
            visited[next_node]=True
            visit_order[next_node]=order
            order+=1
            for i in graph[next_node]:
                if visited[i]==False:
                    stack.append(i)
dfs(r)
for i in range(1,n+1):
    print(visit_order.get(i,0))