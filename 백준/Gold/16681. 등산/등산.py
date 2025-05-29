import collections
import sys
from heapq import heappop,heappush

def dijkstra(start):
    distance=[sys.maxsize for _ in range(N+1)]
    distance[start]=0
    heap=[(0,start)]

    while heap:
        cost,node=heappop(heap)
        if cost>distance[node]:
            continue

        for adj,adj_dist in graph[node]:
            if heights[node]>=heights[adj]:
                continue
            n_cost=cost+adj_dist*D
            if distance[adj]>n_cost:
                distance[adj]=n_cost
                heappush(heap,(n_cost,adj))

    return distance

N, M, D, E = map(int, sys.stdin.readline().split())
heights = [0] + list(map(int, sys.stdin.readline().split()))
graph = collections.defaultdict(list)
for _ in range(M):
    a,b,n=map(int, sys.stdin.readline().split())
    graph[a].append((b,n))
    graph[b].append((a,n))

home_to_target_distance=dijkstra(1)
school_to_target_distance=dijkstra(N)
answer=-sys.maxsize
for i in range(2,N):
    if home_to_target_distance[i]!=sys.maxsize and school_to_target_distance[i]!=sys.maxsize:
        accomplishment=heights[i]*E
        paid_health=home_to_target_distance[i]+school_to_target_distance[i]
        answer=max(answer,accomplishment-paid_health)

print(answer if answer!=-sys.maxsize else 'Impossible')