import collections
import sys

w, h = map(int, sys.stdin.readline().split())
board = list(list(sys.stdin.readline().rstrip()) for _ in range(h))
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
direction = ['top', 'down', 'left', 'right']


def bfs(s_r, s_c):
    q = collections.deque([(0, s_r, s_c, 'init')])
    visited = [[[sys.maxsize] * 4 for _ in range(w)] for _ in range(h)]
    for i in range(4):
        visited[s_r][s_c][i]=0
    board[s_r][s_c] = '.'
    answer_point = tuple()
    while q:
        turn_cnt, row, col, dir = q.popleft()
        if board[row][col] == 'C':
            answer_point = (row, col)
            continue
        for i in range(4):
            n_row = row + dy[i]
            n_col = col + dx[i]
            n_dir = direction[i]

            if n_row < 0 or n_col < 0 or n_row > h - 1 or n_col > w - 1 or board[n_row][n_col] == '*':
                continue

            if dir != 'init' and dir != n_dir:
                if turn_cnt + 1 < visited[n_row][n_col][i]:
                    visited[n_row][n_col][i] = turn_cnt + 1
                    q.append((turn_cnt + 1, n_row, n_col, n_dir))
            else:
                if turn_cnt < visited[n_row][n_col][i]:
                    visited[n_row][n_col][i] = turn_cnt
                    q.append((turn_cnt, n_row, n_col, n_dir))

    return min(visited[answer_point[0]][answer_point[1]])


for i in range(h):
    for j in range(w):
        if board[i][j] == 'C':
            print(bfs(i, j))
            exit()
