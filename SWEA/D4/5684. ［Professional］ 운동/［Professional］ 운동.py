import collections
from heapq import heappush, heappop

def dijkstra(start):
    q=[(0,start)]
    distance=[float('inf') for _ in range(N+1)]

    while q:
        cur_dist,cur_node=heappop(q)
        if cur_dist>distance[cur_node]:
            continue

        for next_node,next_cost in graph[cur_node]:
            if cur_dist+next_cost<distance[next_node]:
                heappush(q,(cur_dist+next_cost,next_node))
                distance[next_node]=cur_dist+next_cost

    return distance
T=int(input())
for test_case in range(1,T+1):
    N,M=map(int,input().split())
    graph=collections.defaultdict(list)
    for _ in range(M):
        s,e,c=map(int,input().split())
        graph[s].append((e,c))

    answer=float('inf')

    for i in range(1,N+1):
        answer=min(answer,dijkstra(i)[i])

    if answer==float('inf'):
        answer=-1
    print(f'#{test_case} {answer}')