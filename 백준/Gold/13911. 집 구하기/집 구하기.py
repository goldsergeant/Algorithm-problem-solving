import collections
import sys
from heapq import heappop,heappush,heapify
def dijkstra(start_points):
    heap=[]
    distance=[sys.maxsize for _ in range(V+1)]
    for node in start_points:
        distance[node]=0
        heappush(heap,(0,node))

    while heap:
        dist,node=heappop(heap)
        if dist>distance[node]:
            continue

        for adj,adj_dist in graph[node]:
            n_dist=dist+adj_dist
            if n_dist<distance[adj]:
                distance[adj]=n_dist
                heappush(heap,(n_dist,adj))

    return distance

V,E=map(int,sys.stdin.readline().split())
graph=collections.defaultdict(list)
for _ in range(E):
    u,v,w=map(int,sys.stdin.readline().split())
    graph[u].append((v,w))
    graph[v].append((u,w))

M,X=map(int,sys.stdin.readline().split())
mcdonalds=list(map(int,sys.stdin.readline().split()))
S,Y=map(int,sys.stdin.readline().split())
starbucks=list(map(int,sys.stdin.readline().split()))
is_house=[True for _ in range(V+1)]

for n in mcdonalds:
    is_house[n]=False
for n in starbucks:
    is_house[n]=False

mcdonald_distance=dijkstra(mcdonalds)
starbucks_distance=dijkstra(starbucks)

answer=sys.maxsize
for i in range(1,V+1):
    if mcdonald_distance[i]<=X and starbucks_distance[i]<=Y and is_house[i]:
        answer=min(answer,mcdonald_distance[i]+starbucks_distance[i])
        
print(answer if answer!=sys.maxsize else -1)