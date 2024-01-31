import collections
import sys
from heapq import heappop,heappush

N,M=map(int,sys.stdin.readline().split())
graph=collections.defaultdict(list)
for _ in range(M):
    a,b,c=map(int,sys.stdin.readline().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstra():
    distance=[sys.maxsize]*(N+1)
    distance[1]=0
    heap=[(0,1)]

    while heap:
        dist,node=heappop(heap)
        if dist>distance[node]:
            continue

        for next_node,next_dist in graph[node]:
            if distance[next_node]>dist+next_dist:
                distance[next_node]=dist+next_dist
                heappush(heap,(distance[next_node],next_node))

    return distance

print(dijkstra()[N])
