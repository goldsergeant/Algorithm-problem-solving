import collections
import sys
from heapq import heappush,heappop

def prim(is_max):
    heap=[(0,0)]
    visited=[False for _ in range(N+1)]
    total_cost=0

    while heap:
        cost,node=heappop(heap)
        if is_max:
            cost=-cost
        if visited[node]:
            continue
        visited[node]=True
        total_cost+=cost

        for next_node,next_is_hill in graph[node]:
            if not visited[next_node]:
                if is_max:
                    heappush(heap,(-next_is_hill,next_node))
                else:
                    heappush(heap, (next_is_hill, next_node))

    return total_cost**2



N,M=map(int,sys.stdin.readline().split())
graph=collections.defaultdict(list)

for _ in range(M+1):
    a,b,c=map(int,sys.stdin.readline().split())
    c=0 if c==1 else 1
    graph[a].append((b,c))
    graph[b].append((a,c))

print(prim(True)-prim(False))