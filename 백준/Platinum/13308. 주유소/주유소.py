import collections
import sys
from heapq import heappush, heappop

N, M = map(int, sys.stdin.readline().split())
liters = [0] + list(map(int, sys.stdin.readline().split()))
graph = collections.defaultdict(list)
for _ in range(M):
    u, v, c = map(int, sys.stdin.readline().split())
    graph[u].append((v, c))
    graph[v].append((u, c))

heap = [(0, 1, liters[1])]
distance = [[sys.maxsize for _ in range(2500 + 1)] for _ in range(N + 1)]
while heap:
    total_cost, node, min_liter_cost = heappop(heap)
    min_liter_cost = min(min_liter_cost, liters[node])
    if distance[node][min_liter_cost] < total_cost:
        continue

    for next_node, next_length in graph[node]:
        if total_cost + min_liter_cost * next_length < distance[next_node][min_liter_cost]:
            distance[next_node][min_liter_cost] = total_cost + min_liter_cost * next_length
            heappush(heap, (distance[next_node][min_liter_cost], next_node, min_liter_cost))

print(min(distance[N]))
