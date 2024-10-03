import collections
import sys
from heapq import heappush, heappop

def dijkstra(start):
    distance=[sys.maxsize for _ in range(N+1)]
    q=[]
    heappush(q,(0,start))
    distance[start]=0

    while q:
        cur_dist,cur_node = heappop(q)
        if cur_dist>distance[cur_node]:
            continue

        for next_node,next_dist in graph[cur_node]:
            if cur_dist+next_dist<distance[next_node]:
                distance[next_node]=cur_dist+next_dist
                heappush(q,(distance[next_node],next_node))

    return distance

def dfs(node):
    if node==1:
        return 1
    if dp[node]!=-1:
        return dp[node]

    dp[node]=0

    for next_node,next_dist in graph[node]:
        if shortest_distance[node]<shortest_distance[next_node]:
            dp[node]+= dfs(next_node)
    return dp[node]

N,M=map(int,sys.stdin.readline().split())
graph=collections.defaultdict(list)
dp=[-1 for _ in range(N+1)]

for _ in range(M):
    u,v,c=map(int,sys.stdin.readline().split())
    graph[u].append((v,c))
    graph[v].append((u,c))

shortest_distance=dijkstra(2)



print(dfs(2))