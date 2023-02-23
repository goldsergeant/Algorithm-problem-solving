import collections
import sys

n,m=map(int,sys.stdin.readline().split())
graph=collections.defaultdict(list)
hacking_count=[0 for i in range(n+1)]
for _ in range(m):
    a,b=map(int,sys.stdin.readline().split())
    graph[b].append(a)

def dfs(node):
    visited=[False for i in range(n+1)]
    stack=collections.deque()
    stack.append(node)
    while stack:
        next_node=stack.pop()
        if not visited[next_node]:
            visited[next_node]=True
            hacking_count[node]+=1
            for i in graph[next_node]:
                stack.append(i)

for i in range(1,n+1):
    dfs(i)

for i in range(len(hacking_count)):
    if hacking_count[i]==max(hacking_count):
        print(i,end=' ')