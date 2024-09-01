import collections
import sys
from heapq import heappush, heappop

N,M=map(int,sys.stdin.readline().split())
graph=[[] for _ in range(N+1)]
distance=[sys.maxsize for _ in range(N+1)]
visited=[False for _ in range(N+1)]
heap=[]

for i in range(1,M+1):
    u,v=map(int,sys.stdin.readline().split())
    graph[u].append((v,i))
    graph[v].append((u,i))
    if sorted((u,v))[0]==1:
        distance[1]=0
        heappush(heap,(0,1))

while heap:
    time,node=heappop(heap)
    if distance[node]<time or visited[node]:
        continue

    visited[node]=True
    cur_period=time%M
    for next_node,next_period in graph[node]:
        if visited[next_node]:
            continue
        next_time=(time//M)*M+next_period if cur_period<next_period else (time//M+1)*M+next_period
        if distance[next_node]<=next_time:
            continue
        distance[next_node]=next_time
        heappush(heap,(distance[next_node],next_node))

print(distance[N])
