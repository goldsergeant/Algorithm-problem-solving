import collections
import sys
from heapq import heappush,heappop


def solution(n, roads, sources, destination):
    def dijkstra(start):
        q=[(0,start)]
        distance=[sys.maxsize for _ in range(n+1)]
        distance[start]=0
        
        while q:
            cost,node=heappop(q)
            if cost>distance[node]:
                continue
            
            for next_node in graph[node]:
                if cost+1<distance[next_node]:
                    distance[next_node]=cost+1
                    heappush(q,(cost+1,next_node))
        return distance
    
    dp = [-1 for _ in range(n + 1)]
    answer = []
    graph = collections.defaultdict(list)

    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
    
    distance=dijkstra(destination)
    
    for node in sources:
        val=distance[node]
        answer.append(-1 if val==sys.maxsize else val)

    return answer

print(solution(3, [[1, 2], [2, 3]], [2, 3], 1))