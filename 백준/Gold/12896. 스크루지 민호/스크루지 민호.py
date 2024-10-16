import collections
import math
import sys
sys.setrecursionlimit(1000000)

def dfs(node,depth):
    global last_tup
    if depth>last_tup[1]:
        last_tup=(node,depth)

    visited[node] = True
    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node,depth+1)

N=int(sys.stdin.readline())
graph=collections.defaultdict(list)
for _ in range(N-1):
    u,v=map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

last_tup=(0,0)
visited=[False for _ in range(N+1)]
dfs(1,0)
last_tup=(last_tup[0],0)
visited=[False for _ in range(N+1)]
dfs(last_tup[0],0)
# print(last_tup)
print(math.ceil(last_tup[1]/2))