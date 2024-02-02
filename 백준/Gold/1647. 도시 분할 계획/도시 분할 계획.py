import collections
from heapq import heappush, heappop
import sys

N, M = map(int, sys.stdin.readline().split())
graph = collections.defaultdict(list)
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def prim(start):
    heap = [(0, start)]
    visited = [False] * (N + 1)
    edge_costs = []
    while heap:
        cost, node = heappop(heap)
        if not visited[node]:
            visited[node] = True
            edge_costs.append(cost)
            for next_node, next_cost in graph[node]:
                if not visited[next_node]:
                    heappush(heap, (next_cost, next_node))
    return edge_costs

costs = prim(1)
costs.sort(reverse=True)
print(sum(costs[1:]))
