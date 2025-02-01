import collections
import sys
from heapq import heappush, heappop

N, M, K = map(int, sys.stdin.readline().split())
graph = collections.defaultdict(list)
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))


def dijkstra(start):
    heap = [(0, start)]
    distance = [[] for _ in range(N + 1)]
    distance[start].append(0)

    while heap:
        cost, node = heappop(heap)

        for next_node, next_cost in graph[node]:
            if len(distance[next_node]) < K:
                heappush(distance[next_node], -(cost + next_cost))
                heappush(heap, (cost + next_cost, next_node))
            else:
                if cost + next_cost < -distance[next_node][0]:
                    heappop(distance[next_node])
                    heappush(distance[next_node], -(cost + next_cost))
                    heappush(heap, (cost + next_cost, next_node))

    return distance


distance = dijkstra(1)
for i in range(1, N + 1):
    if len(distance[i]) < K:
        print(-1)
    else:
        print(-distance[i][0])
