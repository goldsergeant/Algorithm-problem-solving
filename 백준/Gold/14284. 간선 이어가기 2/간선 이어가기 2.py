import collections
import sys
from heapq import heappop,heappush

def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

def union(a,b):
    a=find(a)
    b=find(b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

def dijkstra(start):
    distance=[sys.maxsize for _ in range(N+1)]
    heap=[(0,start)]
    distance[start]=0

    while heap:
        cost,cur=heappop(heap)

        if cost>distance[cur]:
            continue

        for next_node,next_cost in graph[cur]:
            if next_cost+cost<distance[next_node]:
                distance[next_node]=next_cost+cost
                heappush(heap,(next_cost+cost,next_node))
    return distance


N,M=map(int,sys.stdin.readline().split())
graph=collections.defaultdict(list)
parent=[i for i in range(N+1)]
edges=[list(map(int,sys.stdin.readline().split())) for _ in range(M)]
S,T=map(int,sys.stdin.readline().split())


for a,b,c in edges:
    graph[a].append((b,c))
    graph[b].append((a,c))
    # if find(a)!=find(b):
    #     union(a,b)
    # else:
    #     break

distance=dijkstra(S)
print(distance[T])