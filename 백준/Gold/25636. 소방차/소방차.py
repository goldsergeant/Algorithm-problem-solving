import collections
import sys
from heapq import heappush,heappop

def dijkstra(start):
    distance=[[sys.maxsize,-sys.maxsize] for _ in range(N+1)]
    q=[]

    heappush(q,(0,-waters[start],start))
    distance[start]=[0, waters[start]]

    while q:
        dist,water,node=heappop(q)
        water=-water
        if dist>distance[node][0]:
            continue
        if dist==distance[node][0] and water<distance[node][1]:
            continue

        for next_node,next_distance in graph[node]:
            if dist+next_distance<distance[next_node][0]:
                distance[next_node][0]=dist+next_distance
                distance[next_node][1]=water+waters[next_node]
                heappush(q,(dist+next_distance,-(water+waters[next_node]),next_node))
            elif dist+next_distance==distance[next_node][0] and water+waters[next_node]>distance[next_node][1]:
                distance[next_node][0]=dist+next_distance
                distance[next_node][1]=water+waters[next_node]
                heappush(q,(dist+next_distance,-(water+waters[next_node]),next_node))

    return distance

N=int(sys.stdin.readline())
waters=[0]+list(map(int, sys.stdin.readline().split()))
M=int(sys.stdin.readline())
graph=collections.defaultdict(list)
for _ in range(M):
    u,v,c=map(int,sys.stdin.readline().split())
    graph[u].append((v,c))
    graph[v].append((u,c))

s,e=map(int,sys.stdin.readline().split())
distance=dijkstra(s)

# print(distance)
if distance[e][0]!=sys.maxsize:
    print(*distance[e])
else:
    print(-1)