import collections
import sys
from heapq import heappop,heappush

def bfs():
    q=collections.deque()
    distance=[[0 for _ in range(M+1)] for _ in range(N+1)]
    q.append((1,1))
    while q:
        node,cnt=q.popleft()

        for next_node,next_cost in graph[node].items():
            if cnt+1<=M and distance[node][cnt]+next_cost>distance[next_node][cnt+1]:
                distance[next_node][cnt+1]=distance[node][cnt]+next_cost
                q.append((next_node,cnt+1))

    return distance


N,M,K=map(int,sys.stdin.readline().split())
graph=[collections.defaultdict(int) for _ in range(N+1)]
for _ in range(K):
    a,b,c=map(int,sys.stdin.readline().split())
    if a<b:
        graph[a][b]=max(graph[a][b],c)

print(max(bfs()[N]))