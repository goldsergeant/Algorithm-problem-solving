import collections
import sys


def bfs(visited,s_r,s_c):
    q = collections.deque([(s_r, s_c)])
    visited[s_r][s_c] = 0
    while q:
        r, c = q.popleft()
        for dr, dc in (0, -1), (0, 1), (-1, 0), (1, 0),:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(board) and 0 <= nc < len(board[0]):
                if board[nr][nc] == '#':
                    if visited[r][c] + 1 < visited[nr][nc]:
                        visited[nr][nc] = visited[r][c] + 1
                        q.append((nr, nc))
                elif board[nr][nc] == '.' or board[nr][nc]=='$':
                    if visited[r][c] < visited[nr][nc]:
                        visited[nr][nc] = visited[r][c]
                        q.append((nr, nc))


T = int(sys.stdin.readline())
for t in range(T):
    H, W = map(int, sys.stdin.readline().split())
    board = [list(sys.stdin.readline().rstrip()) for _ in range(H)]
    board = [['.' for _ in range(W + 2)]] + board + [['.' for _ in range(W + 2)]]
    for i in range(1, len(board) - 1):
        board[i] = ['.'] + board[i] + ['.']

    visited1 = [[sys.maxsize for _ in range(W + 2)] for _ in range(H + 2)]
    visited2 = [[sys.maxsize for _ in range(W + 2)] for _ in range(H + 2)]
    visited3 = [[sys.maxsize for _ in range(W + 2)] for _ in range(H + 2)]
    cnt = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '$':
                if cnt == 0:
                    bfs(visited1,i,j)
                    cnt += 1
                else:
                    bfs(visited2,i,j)
    bfs(visited3,0,0)
    answer=sys.maxsize
    for i in range(len(visited3)):
        for j in range(len(visited3[i])):
            if board[i][j] == '#':
                answer=min(answer,visited1[i][j]+visited2[i][j]+visited3[i][j]-2)
            else:
                answer=min(answer,visited1[i][j]+visited2[i][j]+visited3[i][j])

    print(answer)