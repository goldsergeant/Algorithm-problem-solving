import sys
from heapq import heappush, heappop


def solution(board):
    answer = 0
    distance = [[[[sys.maxsize for _ in range(2)] for _ in range(2)] for _ in range(len(board))] for _ in
                range(len(board))]
    heap = []
    for dy, dx in (1, 0), (0, 1):
        if board[dy][dx] == 0:
            distance[0][0][dy][dx] = 100
            heappush(heap, (100, dy, dx, dy, dx))

    while heap:
        cost, y, x, pre_dy, pre_dx = heappop(heap)
        if cost > distance[y][x][pre_dy][pre_dx]:
            continue

        if (y, x) == (len(board) - 1, len(board) - 1):
            return cost

        for dy, dx in (-1, 0), (1, 0), (0, -1), (0, 1):
            ny, nx = y + dy, x + dx
            if 0 <= ny < len(board) and 0 <= nx < len(board[0]) and board[ny][nx] == 0:
                next_cost = cost + 100 if (dy, dx) == (pre_dy, pre_dx) else cost + 600
                if next_cost < distance[ny][nx][pre_dy][pre_dx]:
                    distance[ny][nx][pre_dy][pre_dx] = next_cost
                    heappush(heap, (next_cost, ny, nx, dy, dx))
