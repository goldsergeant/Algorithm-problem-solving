import collections
import sys
from heapq import heappop, heappush

N,M,T=map(int,sys.stdin.readline().split())
graph=collections.defaultdict(list)
answer=0
conquer_cost=0
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

visited=[False for _ in range(N+1)]
heap=[(0,1)]

while heap:
    cost,node=heappop(heap)

    if not visited[node]:
        visited[node]=True
        answer+=cost+conquer_cost

        if node!=1:
            conquer_cost+=T

        for next_node,next_cost in graph[node]:
            if not visited[next_node]:
                heappush(heap,(next_cost,next_node))


print(answer)