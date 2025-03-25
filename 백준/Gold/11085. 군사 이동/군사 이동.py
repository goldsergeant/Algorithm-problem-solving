import collections
import sys
from heapq import heappush,heappop
P,W=map(int,sys.stdin.readline().split())
c,v=map(int,sys.stdin.readline().split())
graph=collections.defaultdict(list)
for _ in range(W):
    s,e,w=map(int,sys.stdin.readline().split())
    graph[s].append((e,w))
    graph[e].append((s,w))

heap=[(-sys.maxsize,c)]
distance=[0 for _ in range(P+1)]
distance[c]=sys.maxsize
narrow_width=sys.maxsize
while heap:
    width,node=heappop(heap)
    width=-width
    narrow_width=min(narrow_width,width)
    if node==v:
        break

    for next_node,next_width in graph[node]:
        n_width=min(width,next_width)
        if distance[next_node]<n_width:
            distance[next_node]=n_width
            heappush(heap,(-n_width,next_node))


print(narrow_width)
