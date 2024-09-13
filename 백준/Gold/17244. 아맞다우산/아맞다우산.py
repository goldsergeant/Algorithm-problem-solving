import collections
import sys

M, N = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
things_cnt = 0
start = (0, 0)
visited = [[[False for _ in range(31 + 1)] for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if board[i][j] == 'X':
            board[i][j] = str(things_cnt)
            things_cnt += 1
        elif board[i][j] == 'S':
            start = (i, j)

q = collections.deque([(start[0], start[1], 0, 0)])
end_code = 0
if things_cnt:
    end_code= int('1'*things_cnt,2)
visited[start[0]][start[1]][0] = True

while q:
    r, c, found_code, cnt = q.popleft()

    if found_code == end_code and board[r][c] == 'E':
        print(cnt)
        break

    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dy, c + dx
        if 0 <= nr < N and 0 <= nc < M and board[nr][nc] != '#':
            if board[nr][nc].isdigit():
                tmp_code = 1 << int(board[nr][nc]) | found_code
                if not visited[nr][nc][tmp_code]:
                    q.append((nr, nc, tmp_code, cnt + 1))
                    visited[nr][nc][tmp_code] = True

            elif not visited[nr][nc][found_code]:
                q.append((nr,nc,found_code,cnt+1))
                visited[nr][nc][found_code] = True
