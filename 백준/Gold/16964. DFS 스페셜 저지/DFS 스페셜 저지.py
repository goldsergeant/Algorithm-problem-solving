import collections
import sys

N=int(input())
graph=collections.defaultdict(list)
visited=[False for _ in range(N+1)]
dfs_order=[]
for _ in range(N-1):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

arr=list(map(int,sys.stdin.readline().split()))
order=[-1 for _ in range(N+1)]

def dfs(node):
    if visited[node]:
        return
    visited[node]=True
    dfs_order.append(node)
    for element in graph[node]:
        if not visited[element]:
            dfs(element)

for i,n in enumerate(arr):
    order[n]=i+1

for key in graph.keys():
    graph[key].sort(key=lambda x:order[x])

dfs(arr[0])

print(1 if dfs_order==arr and arr[0]==1 else 0)


