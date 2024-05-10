import collections
import sys
from heapq import heappush,heappop

def prim():
    heap=[]
    visited=[False for _ in range(N+1)]
    total_cost=0

    for city in installed_cities:
        heappush(heap,(0,city))

    while heap:
        cur_distance,city=heappop(heap)
        if visited[city]:
            continue
        visited[city]=True
        total_cost+=cur_distance

        for next_city,next_distance in graph[city]:
            if not visited[next_city]:
                heappush(heap,(next_distance,next_city))

    return total_cost


N,M,K=map(int,sys.stdin.readline().split())
installed_cities=list(map(int,sys.stdin.readline().split()))
graph=collections.defaultdict(list)
for _ in range(M):
    u,v,w=map(int,sys.stdin.readline().split())
    graph[u].append((v,w))
    graph[v].append((u,w))

print(prim())
