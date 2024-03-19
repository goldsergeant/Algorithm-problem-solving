import collections
import sys
from heapq import heappop,heappush

N,M=map(int,sys.stdin.readline().split())
in_degree= [0] * (N + 1)
graph=collections.defaultdict(list)
for _ in range(M):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    in_degree[b]+=1

heap=[]

for i in range(1,N+1):
    if in_degree[i]==0:
        heappush(heap,i)

while heap:
    node=heappop(heap)
    print(node,end=' ')

    for next_node in graph[node]:
        in_degree[next_node]-=1
        if in_degree[next_node]==0:
            heappush(heap,next_node)
