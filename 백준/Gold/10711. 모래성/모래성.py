import collections
import sys

dy = [0, -1, 0, 1, -1, -1, 1, 1]
dx = [1, 0, -1, 0, -1, 1, -1, 1]


def set_empty_sand_cnt(r, c):
    for i in range(8):
        nr = dy[i] + r
        nc = dx[i] + c
        if nr < 0 or nc < 0 or nr >= H or nc >= W:
            continue
        if board[nr][nc] == '.':
            no_sand_cnt_arr[r][c] += 1


H, W = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(H)]
no_sand_cnt_arr = [[0 for _ in range(W)] for _ in range(H)]
visited=[[False for _ in range(W)] for _ in range(H)]
q = collections.deque()
answer = 0

for i in range(H):
    for j in range(W):
        if board[i][j].isdigit():
            set_empty_sand_cnt(i, j)
            if no_sand_cnt_arr[i][j] >= int(board[i][j]):
                q.append((i, j))
                visited[i][j]=True

while q:
    for _ in range(len(q)):
        r, c = q.popleft()
        board[r][c] = '.'

        for i in range(8):
            nr, nc = r + dy[i], c + dx[i]
            if not board[nr][nc].isdigit() or visited[nr][nc]:
                continue
            no_sand_cnt_arr[nr][nc] += 1
            if no_sand_cnt_arr[nr][nc] >= int(board[nr][nc]):
                visited[nr][nc] = True
                q.append((nr, nc))

    answer += 1

print(answer)
