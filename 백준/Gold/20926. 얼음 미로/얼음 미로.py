import collections
import sys

TERA = 'T'
ROCK = 'R'
HOLE = 'H'
EXIT = 'E'
input = sys.stdin.readline

W, H = map(int, input().split())
board = [list(map(lambda x: int(x) if x.isnumeric() else x, list(input().strip()))) for _ in range(H)]


def get_next_position(cur_r, cur_c, dy, dx):
    r, c = cur_r, cur_c
    while True:
        nr, nc = r + dy, c + dx
        if nr < 0 or nc < 0 or nr >= H or nc >= W:
            return False
        if board[nr][nc] == HOLE:
            return False
        if board[nr][nc] == ROCK:
            return r, c
        if board[nr][nc] == EXIT:
            return nr, nc
        r, c = nr, nc


def get_move_cost(cur_r, cur_c, end_r, end_c, dy, dx):
    r, c = cur_r, cur_c
    cost = 0
    while (r, c) != (end_r, end_c):
        nr, nc = r + dy, c + dx
        if type(board[nr][nc]) == int:
            cost += board[nr][nc]
        r, c = nr, nc
    return cost


q = collections.deque()
distance = [[sys.maxsize for _ in range(W)] for _ in range(H)]
for i in range(H):
    for j in range(W):
        if board[i][j] == TERA:
            q.append((i, j))
            distance[i][j] = 0
            board[i][j] = 0

while q:
    r, c = q.popleft()

    if board[r][c] == EXIT:
        continue

    for dy, dx in (0, 1), (0, -1), (1, 0), (-1, 0),:
        tmp = get_next_position(r, c, dy, dx)
        if tmp == False:
            continue
        nr, nc = tmp
        n_cost = get_move_cost(r, c, nr, nc, dy, dx)

        if n_cost + distance[r][c] < distance[nr][nc]:
            distance[nr][nc] = n_cost + distance[r][c]
            q.append((nr, nc))

for i in range(H):
    for j in range(W):
        if board[i][j] == EXIT:
            print(distance[i][j] if distance[i][j] != sys.maxsize else -1)
            exit()
