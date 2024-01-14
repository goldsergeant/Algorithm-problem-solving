import collections
import math
import sys
from heapq import heappush, heappop

N, M = map(int, sys.stdin.readline().split())
points = [(0, 0)]
graph = collections.defaultdict(list)


def get_dist(x1, y1, x2, y2):
    return (((x2 - x1) ** 2) + ((y2 - y1) ** 2))**0.5


for _ in range(N):
    x, y = map(float, sys.stdin.readline().split())
    points.append((x, y))

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append((v, 0))
    graph[v].append((u, 0))

for i in range(1, N):
    for j in range(i+1, N + 1):
        graph[i].append((j, get_dist(*points[i], *points[j])))
        graph[j].append((i, get_dist(*points[i], *points[j])))


def prim():
    q = [(0,1)]
    visited = [False for _ in range(N + 1)]
    answer = 0

    while q:
        cur_dist, cur_node = heappop(q)
        if not visited[cur_node]:
            answer += cur_dist
            visited[cur_node] = True

            for next_node, next_dist in graph[cur_node]:
                heappush(q, (next_dist, next_node))

    return answer


print('%.2f' % prim())
