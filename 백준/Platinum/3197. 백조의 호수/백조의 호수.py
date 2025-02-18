import collections
import sys

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


# 찬스를 써서 갔으면 2, 그냥 갔으면 1, 안 갔으면 sys.maxsize
def swan_bfs():
    while swan_q1:
        r, c = swan_q1.popleft()
        if board[r][c]=='L' and (s_r,s_c)!=(r,c):
            print(day)
            exit()
        for i in range(4):
            nr, nc = r + dy[i], c + dx[i]
            if 0 <= nr < R and 0 <= nc < C:
                if board[nr][nc] == 'X':
                    if not swan_visited[nr][nc]:
                        swan_visited[nr][nc] = True
                        swan_q2.append((nr, nc))
                else:
                    if not swan_visited[nr][nc]:
                        swan_visited[nr][nc] = True
                        swan_q1.append((nr, nc))


def water_bfs():
    for _ in range(len(water_q)):
        r, c = water_q.popleft()
        board[r][c] = '.'
        for i in range(4):
            nr, nc = r + dy[i], c + dx[i]
            if 0 <= nr < R and 0 <= nc < C:
                if board[nr][nc] == 'X':
                    if not water_visited[nr][nc]:
                        water_visited[nr][nc] = True
                        water_q.append((nr, nc))


R, C = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
swan_q1 = collections.deque()
swan_q2 = collections.deque()
water_q = collections.deque()
s_r, s_c = 0, 0
swan_visited = [[False for _ in range(C)] for _ in range(R)]
water_visited = [[False for _ in range(C)] for _ in range(R)]
for i in range(R):
    for j in range(C):
        if board[i][j] == 'L':
            if not swan_q1:
                swan_q1.append((i, j))
                swan_visited[i][j] = True
                s_r,s_c=i,j

        elif board[i][j] == 'X':
            for k in range(4):
                ni, nj = i + dy[k], j + dx[k]
                if 0 <= ni < R and 0 <= nj < C:
                    if board[ni][nj] != 'X':
                        water_q.append((i, j))

day = 0
while True:
    swan_bfs()
    if not swan_q1 and not swan_q2:
        break
    day += 1
    water_bfs()
    swan_q1, swan_q2 = swan_q2, swan_q1

print(day)
