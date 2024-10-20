import collections
import sys
import math


def get_distance(i, j):
    x1, y1 = gas_stations[i]
    x2, y2 = gas_stations[j]
    return (abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2)**0.5


def check(mid):
    q = collections.deque([(0, 0)])
    visited = [sys.maxsize for _ in range(len(gas_stations))]
    visited[0] = 0

    while q:
        node, cnt = q.popleft()
        if node == len(gas_stations) - 1:
            return True

        for next_node in range(len(gas_stations)):
            if fuel_list[node][next_node] <= mid and cnt <= K and cnt + 1 < visited[next_node]:
                visited[next_node] = cnt + 1
                q.append((next_node, cnt + 1))

    return False


N, K = map(int, sys.stdin.readline().split())
gas_stations = [[0, 0]] + [list(map(int, sys.stdin.readline().split())) for _ in range(N)] + [[10000, 10000]]
fuel_list = [[0 for _ in range(len(gas_stations))] for _ in range(len(gas_stations))]

for i in range(len(gas_stations)):
    for j in range(i + 1, len(gas_stations)):
        fuel_list[i][j] = fuel_list[j][i] = math.ceil(get_distance(i, j)) / 10

left = 0
right = get_distance(0, len(gas_stations) - 1) / 10

while left + 1 < right:
    mid = (left + right) // 2
    # print(left, right, mid)

    if check(mid):
        right = mid
    else:
        left = mid

print(int(right))
