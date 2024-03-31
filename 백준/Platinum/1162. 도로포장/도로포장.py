from heapq import heappop, heappush
import sys

N, M, K = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
distance = [[sys.maxsize for _ in range(K+1)] for _ in range(N+1)]
answer = sys.maxsize
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

heap=[(0,1,0)]

while heap:
    cost,node,use_cnt=heappop(heap)
    if node==N:
        distance[node][use_cnt]=min(distance[node][use_cnt],cost)
        continue

    if cost>distance[node][use_cnt]:
        continue

    for next_node,next_cost in graph[node]:
        if cost+next_cost<distance[next_node][use_cnt]:
            distance[next_node][use_cnt]=cost+next_cost
            heappush(heap,(cost+next_cost,next_node,use_cnt))
        if use_cnt<K and cost<distance[next_node][use_cnt+1]:
            distance[next_node][use_cnt+1]=cost
            heappush(heap,(cost,next_node,use_cnt+1))


print(min(distance[N]))