import collections
import sys
from heapq import heappop, heappush

N, M = map(int, sys.stdin.readline().split())
graph = collections.defaultdict(list)
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

s, e = map(int, sys.stdin.readline().split())
max_weights = [0 for _ in range(N + 1)]
heap = [(-sys.maxsize, s)]

while heap:
    cur_weight, cur_node = heappop(heap)
    cur_weight = -cur_weight

    if cur_node == e:
        print(cur_weight)
        break

    if cur_weight < max_weights[cur_node]:
        continue

    for adj, weight in graph[cur_node]:
        n_weight = min(cur_weight, weight)
        if max_weights[adj] < n_weight:
            max_weights[adj] = n_weight
            heappush(heap, (-n_weight, adj))
