import collections

dir = [(0, -1), (0, 1), (1, 0), (-1, 0)]


def solution(board):
    def in_check(r, c):
        if r < 0 or c < 0 or r > len(board) - 1 or c > len(board[0]) - 1:
            return False
        return True

    def get_n_point(r, c, d):
        nr, nc = r, c
        dr, dc = dir[d]
        while in_check(nr, nc) and board[nr][nc] != 'D':
            nr, nc = nr + dr, nc + dc
        return nr - dr, nc - dc

    answer = 0
    q = collections.deque()
    visited = [[[False for _ in range(4)] for _ in range(len(board[0]))] for _ in range(len(board))]
    e_r, e_c = 0, 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                for d in range(4):
                    q.append((i, j, d, 0))
                    visited[i][j][d] = True
            elif board[i][j] == 'G':
                e_r, e_c = i, j

    while q:
        r, c, d, cnt = q.popleft()
        if (r, c) == (e_r, e_c):
            return cnt

        for n_d in range(4):
            nr, nc = get_n_point(r, c, n_d)
            if visited[nr][nc][n_d]:
                continue
            visited[nr][nc][n_d] = True
            q.append((nr, nc, n_d, cnt + 1))

    return -1