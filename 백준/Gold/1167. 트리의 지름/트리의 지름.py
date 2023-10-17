import collections
import sys

v=int(sys.stdin.readline())
graph=collections.defaultdict(list)
max_node=max_distance=0

for _ in range(v):
    arr=list(map(int,sys.stdin.readline().split()))
    node=arr[0]
    for i in range(1,len(arr)-1,2):
        graph[node].append((arr[i],arr[i+1]))

def dfs(node,total_distance):
    global max_distance,max_node

    visited[node]=True
    if max_distance<total_distance:
        max_distance=total_distance
        max_node=node

    for next_node,next_distance in graph[node]:
        if not visited[next_node]:
            dfs(next_node,total_distance+next_distance)

visited=[False]*(v+1)
dfs(1,0)
visited=[False]*(v+1)
max_distance=0
dfs(max_node,0)
print(max_distance)