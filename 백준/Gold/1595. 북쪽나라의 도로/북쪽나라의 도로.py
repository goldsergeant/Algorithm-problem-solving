import collections
import sys
from heapq import heappush, heappop


def dijkstra(start,max_node):
    q = [(0, start)]
    distance = [sys.maxsize for _ in range(max_node+1)]
    distance[start] = 0

    while q:
        cost, node = heappop(q)
        if cost > distance[node]:
            continue

        for next_node, next_cost in graph[node]:
            if cost + next_cost < distance[next_node]:
                distance[next_node] = cost + next_cost
                heappush(q, (cost + next_cost, next_node))

    return distance


graph = collections.defaultdict(list)
max_node = 1
while True:
    try:
        u, v, c = map(int, sys.stdin.readline().split())
        graph[u].append((v, c))
        graph[v].append((u, c))
        max_node = max(max_node, u, v)
    except ValueError:
        break

root_distance = dijkstra(1,max_node)
longest_node = root_distance.index(max(root_distance[1:]))

print(max(dijkstra(longest_node,max_node)[1:]))
