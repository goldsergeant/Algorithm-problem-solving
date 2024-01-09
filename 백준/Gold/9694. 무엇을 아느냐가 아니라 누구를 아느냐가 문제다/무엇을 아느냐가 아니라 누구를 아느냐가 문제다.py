import collections
from heapq import heappop,heappush
import sys

T=int(sys.stdin.readline())
for t in range(1,T+1):
    N,M=map(int,sys.stdin.readline().split())
    graph=collections.defaultdict(list)
    for _ in range(N):
        x,y,z=map(int,sys.stdin.readline().split())
        graph[x].append((z,y))
        graph[y].append((z,x))

    q=[[0,0,[0]]]
    answer=[]
    distance=[sys.maxsize for _ in range(M)]
    distance[0]=0

    while q:
        cur_dist,cur_node,visited_nodes=heappop(q)

        if cur_dist>distance[cur_node]:
            continue

        for next_dist,next_node in graph[cur_node]:
            if distance[next_node]>cur_dist+next_dist:
                distance[next_node]=cur_dist+next_dist
                if next_node==M-1:
                    answer=visited_nodes+[next_node]
                else:
                    heappush(q,(distance[next_node],next_node,visited_nodes+[next_node]))

    print(f'Case #{t}: {" ".join(map(str,answer)) if answer else -1}')