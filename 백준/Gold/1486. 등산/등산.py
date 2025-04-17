import collections
import sys
from heapq import heappop, heappush


def get_height(ch):
    if ch.isupper():
        return ord(ch) - 65
    else:
        return ord(ch) - 71


def get_go_distance():
    heap = [(0, 0, 0)]
    dist = [[sys.maxsize for _ in range(M)] for _ in range(N)]
    dist[0][0]=0

    while heap:
        t, r, c = heappop(heap)

        for dr, dc in (0, -1), (0, 1), (-1, 0), (1, 0),:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M:
                diff = abs(board[r][c] - board[nr][nc])
                if diff > T:
                    continue
                if board[r][c] >= board[nr][nc]:
                    n_t = t + 1
                    if dist[nr][nc] > n_t:
                        dist[nr][nc] = n_t
                        heappush(heap, (n_t, nr, nc))
                else:
                    n_t = t + diff ** 2
                    if dist[nr][nc] > n_t:
                        dist[nr][nc] = n_t
                        heappush(heap, (n_t, nr, nc))
    return dist


def get_comeback_distance(s_r, s_c):
    heap = [(0, s_r, s_c)]
    dist = [[sys.maxsize for _ in range(M)] for _ in range(N)]
    dist[s_r][s_c] = 0

    while heap:
        t, r, c = heappop(heap)
        if (r, c) == (0, 0):
            return t

        for dr, dc in (0, -1), (0, 1), (-1, 0), (1, 0),:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M:
                diff = abs(board[r][c] - board[nr][nc])
                if diff > T:
                    continue
                if board[r][c] >= board[nr][nc]:
                    n_t = t + 1
                    if dist[nr][nc] > n_t:
                        dist[nr][nc] = n_t
                        heappush(heap, (n_t, nr, nc))
                else:
                    n_t = t + diff ** 2
                    if dist[nr][nc] > n_t:
                        dist[nr][nc] = n_t
                        heappush(heap, (n_t, nr, nc))
    return sys.maxsize


N, M, T, D = map(int, sys.stdin.readline().split())
board = [list(map(lambda x: get_height(x), sys.stdin.readline().strip())) for _ in range(N)]
comeback_distance = [[sys.maxsize for _ in range(M)] for _ in range(N)]
go_distance=get_go_distance()
answer=0
for i in range(N):
    for j in range(M):
        comeback_distance[i][j] = get_comeback_distance(i, j)

for i in range(N):
    for j in range(M):
        if go_distance[i][j]+comeback_distance[i][j]<=D:
            answer=max(answer,board[i][j])

print(answer)