import collections
import sys

N, M = map(int, sys.stdin.readline().split())
distance = [-sys.maxsize for _ in range(N + 1)]
path = [0 for _ in range(N + 1)]
edges = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]


def bellman_ford():
    distance[1] = 0
    for i in range(N):
        for u, v, w in edges:
            if distance[u] > -sys.maxsize and distance[u] + w > distance[v]:
                distance[v] = distance[u] + w
                path[v] = u
                if i == N - 1:
                    distance[v] = sys.maxsize


bellman_ford()
if distance[N] < sys.maxsize:
    answer = []
    cur = N
    while cur != 0:
        answer.append(cur)
        cur = path[cur]

    print(*answer[::-1])
else:
    print(-1)
