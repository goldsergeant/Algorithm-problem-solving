import collections
import sys
sys.setrecursionlimit(100000)
input=sys.stdin.readline
n=int(input())
graph=collections.defaultdict(list)
max_node=0
max_distance=0

for _ in range(n-1):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dfs(node,total_distance):
    global max_distance,max_node
    visited[node]=True
    if total_distance>max_distance:
        max_node=node
        max_distance=total_distance

    for next_node,next_distance in graph[node]:
        if not visited[next_node]:
            dfs(next_node,total_distance+next_distance)


visited=[False]*(n+1)
dfs(1,0)
max_distance=0
visited=[False]*(n+1)
dfs(max_node,0)

print(max_distance)