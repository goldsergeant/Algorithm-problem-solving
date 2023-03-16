import collections
import heapq
import sys

v,e=map(int,sys.stdin.readline().split())
graph=collections.defaultdict(list)
heap=[]
distance=[[sys.maxsize for _ in range(v+1)] for _ in range(v+1)]
for _ in range(e):
    a,b,c=map(int,sys.stdin.readline().split())
    graph[a].append((b,c))
    heapq.heappush(heap,(c,a,b))
    distance[a][b]=c

while heap:
    c,a,b=heapq.heappop(heap)
    if a==b:
        print(c)
        exit()
    if c>distance[a][b]:
        continue

    for next_vertex,next_dist in graph[b]:
        if distance[a][next_vertex]>next_dist+c:
            distance[a][next_vertex]=next_dist+c
            heapq.heappush(heap,(distance[a][next_vertex],a,next_vertex))
print(-1)