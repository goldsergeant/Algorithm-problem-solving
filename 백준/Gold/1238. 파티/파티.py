import collections
import heapq
import sys

n,m,x=map(int,sys.stdin.readline().split())
roads=collections.defaultdict(list)
answer=0

def dijkstra(start,end):
    distance=[sys.maxsize for _ in range(n+1)]
    distance[start]=0
    q=[(distance[start],start)]

    while q:
        cur_distance,cur_node=heapq.heappop(q)
        if distance[cur_node]<cur_distance:
            continue

        for next_node,next_distance in roads[cur_node]:
            if cur_distance+next_distance<distance[next_node]:
                distance[next_node]=cur_distance+next_distance
                heapq.heappush(q,(distance[next_node],next_node))
    return distance[end]


for _ in range(m):
    start,end,t=map(int,sys.stdin.readline().split())
    roads[start].append((end,t))

for i in range(1,n+1):
    if i==x:
        continue
    answer=max(answer,dijkstra(i,x)+dijkstra(x,i))

print(answer)
