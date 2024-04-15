import collections
import sys

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
h, w, s_r, s_c, f_r, f_c = map(int, sys.stdin.readline().split())
dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]


def is_valid_square(r, c):  # 왼쪽 위 좌표
    if r + h - 1 >= N or c + w - 1 >= M or r < 0 or c < 0:
        return False
    return True

def check_block_vertical(s_r, e_r, c):
    for i in range(s_r, e_r + 1):
        if board[i][c] == 1:
            return False
    return True


def check_block_horizontal(r, s_c, e_c):
    for i in range(s_c, e_c + 1):
        if board[r][i] == 1:
            return False
    return True


def bfs():
    q = collections.deque([(s_r - 1, s_c - 1, 0)])
    visited = [[False for _ in range(M)] for _ in range(N)]
    visited[s_r - 1][s_c - 1] = True
    while q:
        r, c, cnt = q.popleft()
        if r == f_r - 1 and c == f_c - 1:
            return cnt
        for i in range(4):  # 오른쪽,왼쪽,위,아래
            n_r, n_c = r + dy[i], c + dx[i]
            n_l_t = (n_r, n_c)
            n_r_t = (n_r, n_c + w - 1)
            n_l_b = (n_r + h - 1, n_c)
            n_r_b = (n_r + h - 1, n_c + w - 1)
            if not is_valid_square(n_r, n_c):
                continue
            if visited[n_r][n_c]:
                continue

            if i == 0:
                if not check_block_vertical(n_r_t[0], n_r_b[0], n_r_t[1]):
                    continue
            elif i == 1:
                if not check_block_vertical(n_l_t[0], n_l_b[0], n_l_t[1]):
                    continue
            elif i == 2:
                if not check_block_horizontal(n_l_t[0], n_l_t[1], n_r_t[1]):
                    continue
            elif i == 3:
                if not check_block_horizontal(n_l_b[0], n_l_b[1], n_r_b[1]):
                    continue

            visited[n_r][n_c] = True
            q.append((n_r, n_c, cnt + 1))

    return -1

print(bfs())