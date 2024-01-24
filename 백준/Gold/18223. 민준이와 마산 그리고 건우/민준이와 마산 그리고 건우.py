import collections
import sys
from heapq import heappush,heappop

V,E,P=map(int,sys.stdin.readline().split())
graph=collections.defaultdict(list)
for _ in range(E):
    a,b,c=map(int,sys.stdin.readline().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstra(graph):
    heap=[(0,1,[1])] # cur_dist,cur_node,visited_nodes
    distance=[sys.maxsize]*(V+1)
    distance[1]=0

    shortest_routes=[]

    while heap:
        cur_dist,cur_node,visited_nodes=heappop(heap)
        if cur_dist>distance[cur_node]:
            continue

        if cur_node==V:
            shortest_routes.append(visited_nodes)
            continue

        for next_node,next_dist in graph[cur_node]:
            if cur_dist+next_dist<=distance[next_node]:
                distance[next_node]=cur_dist+next_dist
                heappush(heap,(distance[next_node],next_node,visited_nodes+[next_node]))

    return shortest_routes

shortest_routes=dijkstra(graph)

for route in shortest_routes:
    if P in route:
        print('SAVE HIM')
        exit()

print('GOOD BYE')