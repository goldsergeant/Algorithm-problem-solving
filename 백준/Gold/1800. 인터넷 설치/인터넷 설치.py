import collections
import sys
from heapq import heappush,heappop

N,P,K=map(int,sys.stdin.readline().split())
graph=collections.defaultdict(list)
for _ in range(P):
    u,v,c=map(int,sys.stdin.readline().split())
    graph[u].append((v,c))
    graph[v].append((u,c))

distance=[[sys.maxsize for _ in range(K+1)] for _ in range(N+1)]
distance[1][0]=0
heap=[(0,1,0)]

while heap:
    cost,node,use_chance_cnt=heappop(heap)
    if cost>distance[node][use_chance_cnt]:
        continue
    if node==N:
        print(cost)
        exit()

    for next_node,next_cost in graph[node]:
        n_cost=max(cost,next_cost)
        if n_cost<distance[next_node][use_chance_cnt]:
            distance[next_node][use_chance_cnt]=n_cost
            heappush(heap,(n_cost,next_node,use_chance_cnt))

        if use_chance_cnt+1<=K:
            if cost<distance[next_node][use_chance_cnt+1]:
                distance[next_node][use_chance_cnt+1]=cost
                heappush(heap,(cost,next_node,use_chance_cnt+1))

print(-1)