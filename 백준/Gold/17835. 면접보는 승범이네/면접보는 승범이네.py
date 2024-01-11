import collections
import sys
from heapq import heappop,heappush

N,M,K=map(int,sys.stdin.readline().split())
graph=collections.defaultdict(list)
interview_spots=[]
distance_arr=[]
min_distance=[sys.maxsize]*(N+1)
for _ in range(M):
    u,v,c=map(int,sys.stdin.readline().split())
    graph[v].append((u,c))

interview_spots.extend(list(map(int,sys.stdin.readline().split())))

def dijkstra():
    distance=[sys.maxsize]*(N+1)
    q=[]
    for spot in interview_spots:
        heappush(q,(0,spot))
        distance[spot]=0

    while q:
        cur_dist,cur_node=heappop(q)
        if cur_dist>distance[cur_node]:
            continue

        for next_node,next_dist in graph[cur_node]:
            if cur_dist+next_dist<distance[next_node]:
                distance[next_node]=cur_dist+next_dist
                heappush(q,(distance[next_node],next_node))

    return distance


distance=dijkstra()
max_dist=max(distance[1:])
print(distance.index(max_dist))
print(max_dist)
