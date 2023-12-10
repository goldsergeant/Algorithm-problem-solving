import collections
import sys

RAINBOW = 0
BLACK = -1
REMOVE = -2

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
score = 0


def gravity():
    for i in range(N - 2, -1, -1):
        for j in range(N):
            if board[i][j] == BLACK:
                continue

            row = i
            while 0 <= row + 1 < N and board[row + 1][j] == REMOVE:
                board[row + 1][j], board[row][j] = board[row][j], REMOVE
                row += 1


def rotate_left():
    new_board = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_board[N - 1 - j][i] = board[i][j]

    return new_board


def search(row, col):
    q = collections.deque([(row, col)])
    block_cnt, rainbow_cnt = 1, 0
    normal_blocks, rainbows = [(row, col)], []
    visited[i][j] = True

    while q:
        cur_r, cur_c = q.popleft()
        for d_y, d_x in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            n_y = cur_r + d_y
            n_x = cur_c + d_x
            if n_y < 0 or n_x < 0 or n_y > N - 1 or n_x > N - 1:
                continue

            if board[n_y][n_x] == board[row][col] or board[n_y][n_x] == RAINBOW:
                if not visited[n_y][n_x]:
                    visited[n_y][n_x] = True
                    q.append((n_y, n_x))
                    block_cnt += 1
                    if board[n_y][n_x] == RAINBOW:
                        rainbow_cnt += 1
                        rainbows.append((n_y, n_x))
                    else:
                        normal_blocks.append((n_y, n_x))

    for y, x in rainbows:
        visited[y][x] = False

    return block_cnt, rainbow_cnt, normal_blocks + rainbows


while True:
    groups = []
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] != REMOVE and board[i][j] != BLACK and board[i][j] != RAINBOW and not visited[i][j]:
                groups.append(search(i, j))

    groups = list(filter(lambda x: x[0] >= 2, groups))
    if not groups:
        break
    groups.sort(reverse=True)
    selected_groups = groups[0]
    score += selected_groups[0] ** 2
    for y, x in selected_groups[2]:
        board[y][x] = REMOVE

    gravity()
    board = rotate_left()
    gravity()

print(score)
