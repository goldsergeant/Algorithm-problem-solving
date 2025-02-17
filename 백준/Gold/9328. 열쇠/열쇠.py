import collections
import sys


def bfs(s_r, s_c):
    global answer, got_key
    q = collections.deque([(s_r, s_c)])
    visited[s_r][s_c] = True
    while q:
        r, c = q.popleft()
        if board[r][c] == '$':
            answer += 1
            board[r][c] = '.'
        elif board[r][c].islower():  # 열쇠인 경우
            if board[r][c] not in keys:
                got_key = True
                keys.add(board[r][c])

        for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < h and 0 <= nc < w:
                if board[nr][nc] == '*':
                    continue
                if board[nr][nc].isupper() and board[nr][nc].lower() not in keys:
                    continue
                if visited[nr][nc]:
                    continue
                visited[nr][nc] = True
                q.append((nr, nc))


T = int(sys.stdin.readline())
for _ in range(T):
    h, w = map(int, sys.stdin.readline().split())
    board = [list(sys.stdin.readline().rstrip()) for _ in range(h)]
    keys = set(sys.stdin.readline().rstrip())
    answer = 0
    while True:
        visited = [[False for _ in range(w)] for _ in range(h)]
        got_key = False
        for i in range(h):
            if i == 0 or i == h - 1:  # 끝자락
                for j in range(w):
                    if board[i][j] == '.' or board[i][j] == '$' or board[i][j].islower():
                        if not visited[i][j]:
                            bfs(i, j)
                    elif board[i][j].isupper():
                        if board[i][j].lower() in keys and not visited[i][j]:
                            bfs(i, j)

            else:
                if board[i][0] == '.' or board[i][0] == '$' or board[i][0].islower():
                    if not visited[i][0]:
                        bfs(i, 0)
                elif board[i][0].isupper():
                    if board[i][0].lower() in keys and not visited[i][0]:
                        bfs(i, 0)
                if board[i][w - 1] == '.' or board[i][w - 1] == '$' or board[i][w - 1].islower():
                    if not visited[i][w - 1]:
                        bfs(i, w - 1)
                elif board[i][w - 1].isupper():
                    if board[i][w - 1].lower() in keys and not visited[i][w - 1]:
                        bfs(i, w - 1)
        if not got_key:
            break

    print(answer)
