import collections
from heapq import heappush, heappop
import sys

def dijkstra(remove_edge_num=-1):
    distance=[sys.maxsize for _ in range(N+1)]
    distance[1]=0
    edges=[]
    heap=[(0,1,[])]

    while heap:
        cost,node,visited_edges=heappop(heap)
        if cost>distance[node]:
            continue
        if node==N:
            edges=visited_edges
        for next_node,next_cost,next_edge_num in graph[node]:
            if cost+next_cost<distance[next_node] and next_edge_num!=remove_edge_num:
                distance[next_node]=cost+next_cost
                heappush(heap,(distance[next_node],next_node,visited_edges+[next_edge_num]))

    return distance,edges

N,M=map(int,sys.stdin.readline().split())
graph=collections.defaultdict(list)
for i in range(M):
    a,b,cost=map(int,sys.stdin.readline().split())
    graph[a].append((b,cost,i))
    graph[b].append((a,cost,i))

answer=0
distance,visited_edges=dijkstra(-1)
shortest_time=distance[N]
for i in visited_edges:
    distance,visited_edges=dijkstra(i)
    if distance[N]==sys.maxsize:
        answer=-1
        break
    else:
        answer=max(answer,distance[N]-shortest_time)

print(answer)