import collections
import sys


def time_wall_out_check(r, c):
    if r < 0 or c < 0 or r > M - 1 or c > M - 1:
        return True
    return False


def time_wall_bfs(r, c, state, turn, board):
    for dr, dc in q_dir:
        next_r, next_c = r + dr, c + dc
        if time_wall_out_check(next_r, next_c):
            continue
        if not time_wall_visited[next_r][next_c][state] and board[next_r][next_c] == EMPTY:
            time_wall_visited[next_r][next_c][state] = True
            q.append((next_r, next_c, state, turn))


def miji_out_check(r, c):
    if r < 0 or c < 0 or r > N - 1 or c > N - 1:
        return True
    return False


def miji_bfs(r, c, turn):
    for dr, dc in q_dir:
        next_r, next_c = r + dr, c + dc
        if miji_out_check(next_r, next_c):
            continue
        if not miji_visited[next_r][next_c] and (
                miji_board[next_r][next_c] == EMPTY or miji_board[next_r][next_c] == EXIT) and turn < \
                miji_time_weird_turn[next_r][next_c]:
            miji_visited[next_r][next_c] = True
            q.append((next_r, next_c, IS_FLOOR, turn))


def time_wall_queueing(r, c, state, turn, board):
    if not time_wall_visited[r][c][state] and board[r][c] == EMPTY:
        time_wall_visited[r][c][state] = True
        q.append((r, c, state, turn))


def floor_queueing(r, c, turn):
    if not miji_visited[r][c]:
        miji_visited[r][c] = True
        q.append((r, c, IS_FLOOR, turn))


def process_time_weird_situation():
    for i in range(len(time_weirds)):
        r, c, d, u = time_weirds[i]
        t = 0
        while not miji_out_check(r, c) and miji_board[r][c] == EMPTY:
            miji_time_weird_turn[r][c] = min(miji_time_weird_turn[r][c], t)
            r, c = r + time_weird_dir[d][0], c + time_weird_dir[d][1]
            t += u


time_weird_dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 동서남북
q_dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
EMPTY = 0
BLOCK = 1
TIME_MACHINE = 2
TIME_WALL = 3
EXIT = 4

IS_TOP = 0
IS_WEST = 1
IS_EAST = 2
IS_NORTH = 3
IS_SOUTH = 4
IS_FLOOR = 5

N, M, F = map(int, input().split())
miji_board = [list(map(int, input().split())) for _ in range(N)]
east_time_board = []
west_time_board = []
south_time_board = []
north_time_board = []
top_time_board = []
time_weirds = []
E_R, E_C = 0, 0

for i in range(N):
    for j in range(N):
        if miji_board[i][j] == EXIT:
            E_R, E_C = i, j

for i in range(5):
    if i == 0:
        east_time_board = [list(map(int, input().split())) for _ in range(M)]
    elif i == 1:
        west_time_board = [list(map(int, input().split())) for _ in range(M)]
    elif i == 2:
        south_time_board = [list(map(int, input().split())) for _ in range(M)]
    elif i == 3:
        north_time_board = [list(map(int, input().split())) for _ in range(M)]
    else:
        top_time_board = [list(map(int, input().split())) for _ in range(M)]

q = collections.deque()
time_wall_visited = [[[False for _ in range(5)] for _ in range(M)] for _ in range(M)]
miji_visited = [[False for _ in range(N)] for _ in range(N)]
miji_time_weird_turn = [[sys.maxsize for _ in range(N)] for _ in range(N)]

for _ in range(F):
    r, c, d, u = map(int, input().split())
    time_weirds.append([r, c, d, u])

for i in range(M):
    for j in range(M):
        if top_time_board[i][j] == TIME_MACHINE:
            q.append((i, j, IS_TOP, 0))
            time_wall_visited[i][j][IS_TOP] = True

WEST_R, WEST_C = 0, 0
EAST_R, EAST_C = 0, 0
NORTH_R, NORTH_C = 0, 0
SOUTH_R, SOUTH_C = 0, 0
is_installed = False
for i in range(N):
    for j in range(N):
        if miji_board[i][j] == TIME_WALL and not is_installed:
            is_installed = True
            WEST_R = i
            WEST_C = j
            EAST_R = i
            EAST_C = j + M - 1
            NORTH_R = i
            NORTH_C = j
            SOUTH_R = i + M - 1
            SOUTH_C = j
process_time_weird_situation()
while q:
    r, c, state, turn = q.popleft()
    if (r, c) == (E_R, E_C) and state == IS_FLOOR:
        print(turn)
        exit()
    if state == IS_FLOOR:  # 바닥
        if miji_board[r][c] == TIME_WALL:
            miji_bfs(r, c, turn)
        else:
            miji_bfs(r, c, turn + 1)
    if state == IS_TOP:  # 동서남북 모두와 맞닿음
        time_wall_bfs(r, c, state, turn + 1, top_time_board)
        if c == 0:  # 서쪽과 맞닿음
            w_r, w_c = 0, r
            time_wall_queueing(w_r, w_c, IS_WEST, turn + 1, west_time_board)
        elif c == M - 1:  # 동쪽과 맞닿음
            e_r, e_c = 0, M - r - 1
            time_wall_queueing(e_r, e_c, IS_EAST, turn + 1, east_time_board)

        if r == 0:  # 북쪽과 맞닿음
            n_r, n_c = 0, M - c - 1
            time_wall_queueing(n_r, n_c, IS_NORTH, turn + 1, north_time_board)
        elif r == M - 1:  # 남쪽과 맞닿음
            s_r, s_c = 0, c
            time_wall_queueing(s_r, s_c, IS_SOUTH, turn + 1, south_time_board)

    elif state == IS_WEST:
        time_wall_bfs(r, c, state, turn + 1, west_time_board)
        if c == 0:  # 북쪽과 맞닿음
            n_r, n_c = r, M - 1
            time_wall_queueing(n_r, n_c, IS_NORTH, turn + 1, north_time_board)
        elif c == M - 1:  # 남쪽과 맞닿음
            s_r, s_c = r, 0
            time_wall_queueing(s_r, s_c, IS_SOUTH, turn + 1, south_time_board)
        if r == 0:  # 윗면과 맞닿음
            t_r, t_c = c, 0
            time_wall_queueing(t_r, t_c, IS_TOP, turn + 1, top_time_board)

        elif r == M - 1:  # 바닥과 맞닿음
            f_r, f_c = WEST_R + c, WEST_C
            floor_queueing(f_r, f_c, turn + 1)

    elif state == IS_EAST:
        time_wall_bfs(r, c, state, turn + 1, east_time_board)
        if c == 0:  # 남쪽과 맞닿음
            s_r, s_c = r, M - 1
            time_wall_queueing(s_r, s_c, IS_SOUTH, turn + 1, south_time_board)
        elif c == M - 1:  # 북쪽과 맞닿음
            n_r, n_c = r, 0
            time_wall_queueing(n_r, n_c, IS_NORTH, turn + 1, north_time_board)
        if r == 0:  # 윗면과 맞닿음
            t_r, t_c = c, M - 1
            time_wall_queueing(t_r, t_c, IS_TOP, turn + 1, top_time_board)

        elif r == M - 1:  # 바닥과 맞닿음
            f_r, f_c = EAST_R + M - 1 - c, EAST_C
            floor_queueing(f_r, f_c, turn + 1)

    elif state == IS_NORTH:
        time_wall_bfs(r, c, state, turn + 1, north_time_board)
        if c == 0:  # 동쪽과 맞닿음
            e_r, e_c = r, M - 1
            time_wall_queueing(e_r, e_c, IS_EAST, turn + 1, east_time_board)
        elif c == M - 1:  # 서쪽과 맞닿음
            w_r, w_c = r, 0
            time_wall_queueing(w_r, w_c, IS_WEST, turn + 1, west_time_board)

        if r == 0:  # 윗면과 맞닿음
            t_r, t_c = 0, M - 1 - c
            time_wall_queueing(t_r, t_c, IS_TOP, turn + 1, top_time_board)

        elif r == M - 1:  # 바닥과 맞닿음
            f_r, f_c = NORTH_R, NORTH_C + M - 1 - c
            floor_queueing(f_r, f_c, turn + 1)

    elif state == IS_SOUTH:
        time_wall_bfs(r, c, state, turn + 1, south_time_board)
        if c == 0:  # 서쪽과 맞닿음
            w_r, w_c = r, M - 1
            time_wall_queueing(w_r, w_c, IS_WEST, turn + 1, west_time_board)
        elif c == M - 1:  # 동쪽과 맞닿음
            e_r, e_c = r, 0
            time_wall_queueing(e_r, e_c, IS_EAST, turn + 1, east_time_board)
        if r == 0:  # 윗면과 맞닿음
            t_r, t_c = M - 1, c
            time_wall_queueing(t_r, t_c, IS_TOP, turn + 1, top_time_board)
        elif r == M - 1:  # 바닥과 맞닿음
            f_r, f_c = SOUTH_R, SOUTH_C + c
            floor_queueing(f_r, f_c, turn + 1)

print(-1)
