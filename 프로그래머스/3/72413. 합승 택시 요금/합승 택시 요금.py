import collections
import sys
from heapq import heappush,heappop

def solution(n, s, a, b, fares):
    answer=sys.maxsize

    graph=collections.defaultdict(list)

    def dijkstra(start,distance):
        heap=[(0,start)]
        distance[start]=0
        while heap:
            cur_dist,cur_node=heappop(heap)
            if distance[cur_node]<cur_dist:
                continue

            for next_node,next_cost in graph[cur_node]:
                next_dist=distance[cur_node]+next_cost
                if next_dist<distance[next_node]:
                    distance[next_node]=next_dist
                    heappush(heap,(distance[next_node],next_node))

    for u,v,c in fares:
        graph[u].append((v,c))
        graph[v].append((u,c))

    distance_a=[sys.maxsize for _ in range(n+1)]
    distance_b=[sys.maxsize for _ in range(n+1)]
    distance_start=[sys.maxsize for _ in range(n+1)]

    dijkstra(a,distance_a)
    dijkstra(b,distance_b)
    dijkstra(s,distance_start)

    for i in range(1,n+1):
        # if i in (s,a,b):
        #     continue
        answer=min(answer,distance_a[i]+distance_b[i]+distance_start[i])
    return answer

print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6, 4, 5, 6, [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]))