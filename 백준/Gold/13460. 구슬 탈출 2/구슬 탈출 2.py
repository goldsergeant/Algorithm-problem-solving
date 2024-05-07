import collections
import sys

BLOCK = '#'
HOLE = 'O'
RED = 'R'
BLUE = 'B'
EMPTY = '.'

N, M = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(N)]


def move(y, x, dy, dx):
    ny, nx,cnt = y, x,0
    while board[ny][nx] != HOLE and board[ny][nx] != BLOCK:
        ny, nx,cnt = ny + dy, nx + dx,cnt+1

    if board[ny][nx] == BLOCK:
        ny, nx,cnt = ny - dy, nx - dx,cnt-1

    return ny, nx,cnt


def bfs(start_red_r, start_red_c, start_blue_r, start_blue_c):
    visited = [[[[False for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in
               range(N)]  # [빨강_r][빨강_c][피랑_r][파랑_c]
    q = collections.deque([(start_red_r, start_red_c, start_blue_r, start_blue_c, 0)])
    visited[start_red_r][start_red_c][start_blue_r][start_blue_c] = True

    while q:
        red_r, red_c, blue_r, blue_c, cnt = q.popleft()
        if board[red_r][red_c] == HOLE and board[blue_r][blue_c] != HOLE:
            return cnt
        if board[blue_r][blue_c] == HOLE:
            continue

        for dy, dx in (-1, 0), (1, 0), (0, -1), (0, 1):
            n_red_r, n_red_c,red_cnt = move(red_r, red_c, dy, dx)
            n_blue_r, n_blue_c,blue_cnt = move(blue_r, blue_c, dy, dx)

            if board[n_red_r][n_red_c] != HOLE and board[n_blue_r][n_blue_c] != HOLE:
                if n_red_r == n_blue_r and n_red_c == n_blue_c:
                    if red_cnt<blue_cnt:
                        n_blue_r,n_blue_c=n_blue_r-dy,n_blue_c-dx
                    else:
                        n_red_r,n_red_c=n_red_r-dy,n_red_c-dx

            if cnt + 1 <= 10 and not visited[n_red_r][n_red_c][n_blue_r][n_blue_c]:
                visited[n_red_r][n_red_c][n_blue_r][n_blue_c] = True
                q.append((n_red_r, n_red_c, n_blue_r, n_blue_c, cnt + 1))

    return -1


red_r, red_c, blue_r, blue_c = 0, 0, 0, 0

for i in range(N):
    for j in range(M):
        if board[i][j] == RED:
            red_r, red_c = i, j
        elif board[i][j] == BLUE:
            blue_r, blue_c = i, j

print(bfs(red_r, red_c, blue_r, blue_c))
