import math
from heapq import heappush, heappop


def get_cost(i, j):
    x1, y1 = islands[i]
    x2, y2 = islands[j]
    dist = math.sqrt(abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2)
    return E * dist ** 2


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    islands = [[0, 0] for _ in range(N)]
    x_positions = list(map(int, input().split()))
    y_positions = list(map(int, input().split()))
    E = float(input())
    for i in range(N):
        islands[i][0] = x_positions[i]
        islands[i][1] = y_positions[i]

    q = []
    heappush(q, (0, 0))
    visited = [False for _ in range(N)]
    answer=0

    while q:
        dist, idx = heappop(q)
        if visited[idx]:
            continue
        answer+=dist
        visited[idx] = True
        for i in range(N):
            if not visited[i]:
                heappush(q,(get_cost(i, idx), i))

    print(f'#{test_case} {round(answer)}')