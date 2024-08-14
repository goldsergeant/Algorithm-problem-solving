import collections
import sys
from heapq import heappush, heappop

N,M=map(int,sys.stdin.readline().split())
graph=collections.defaultdict(list)
distance=[sys.maxsize for _ in range(N+1)]
answer=[]
for _ in range(M):
    u,v,c=map(int,sys.stdin.readline().split())
    graph[u].append((v,c))
    graph[v].append((u,c))

heap=[(0,1,1)]
distance[1]=0

while heap:
    dist,node,parent=heappop(heap)
    if dist>distance[node]:
        continue

    answer.append((parent,node))

    for next_node,next_dist in graph[node]:
        if next_dist+dist<distance[next_node]:
            distance[next_node]=next_dist+dist
            heappush(heap,(dist+next_dist,next_node,node))

print(len(answer)-1)
for tup in answer[1:]:
    print(*tup)