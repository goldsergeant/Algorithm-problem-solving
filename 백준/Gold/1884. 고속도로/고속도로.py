import collections
import sys
from heapq import heappop, heappush


def dijkstra():
    distance = [[sys.maxsize for _ in range(K + 1)] for _ in range(N + 1)]
    heap = [(0, K, 1)]
    distance[1][K] = 0

    while heap:
        l, t, node = heappop(heap)

        if l > distance[node][t]:
            continue

        if node == N:
            return l

        for adj, adj_l, adj_t in graph[node]:
            n_l = l + adj_l
            n_t = t - adj_t
            if n_t < 0:
                continue
            if n_l < distance[adj][n_t]:
                distance[adj][n_t] = n_l
                heappush(heap, (n_l, n_t, adj))

    return -1

K = int(sys.stdin.readline())
N = int(sys.stdin.readline())
R = int(sys.stdin.readline())
graph = collections.defaultdict(list)
for _ in range(R):
    s, d, l, t = map(int, sys.stdin.readline().split())
    graph[s].append((d, l, t))

print(dijkstra())