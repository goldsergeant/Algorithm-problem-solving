import sys
from heapq import heappush, heappop


def get_distance(a, b):
    x1, y1 = pipes[a]
    x2, y2 = pipes[b]

    return (x1 - x2) ** 2 + (y1 - y2) ** 2


def prim():
    heap = [(0, 0)]
    visited = [False for _ in range(len(pipes))]
    # visited[0] = True
    total = 0

    while heap:
        cost, node = heappop(heap)
        if visited[node]:
            continue
        total+=cost
        visited[node]=True

        for i in range(len(pipes)):
            if not visited[i] and get_distance(node, i) >= C:
                heappush(heap, (get_distance(node, i), i))

    return total if all(visited) else -1

N, C = map(int, sys.stdin.readline().split())
pipes = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
print(prim())