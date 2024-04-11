import collections
import sys
from heapq import heappop,heappush

T=int(sys.stdin.readline())
for _ in range(T):
    n,d,c=map(int,sys.stdin.readline().split())
    graph=collections.defaultdict(list)
    for _ in range(d):
        a,b,s=map(int,sys.stdin.readline().split())
        # graph[a].append((b,s))
        graph[b].append((a,s))

    heap=[(0,c)]
    distance=[sys.maxsize for _ in range(n+1)]
    distance[c]=0
    while heap:
        cost,cur=heappop(heap)
        if cost>distance[cur]:
            continue

        for next_node,next_cost in graph[cur]:
            if distance[next_node]>distance[cur]+next_cost:
                distance[next_node]=distance[cur]+next_cost
                heappush(heap,(distance[next_node],next_node))

    cnt,total_time=0,0
    for i in range(1,n+1):
        if distance[i]<sys.maxsize:
            cnt+=1
            total_time=max(total_time,distance[i])

    print(cnt,total_time)