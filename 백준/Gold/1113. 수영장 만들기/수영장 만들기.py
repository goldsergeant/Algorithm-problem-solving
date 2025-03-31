import collections
import sys


def bfs(s_r, s_c):
    q = collections.deque([(s_r, s_c)])
    pool = []
    visited = [[False for _ in range(M)] for _ in range(N)]
    visited[s_r][s_c] = True
    standard_height=board[s_r][s_c]
    min_height = sys.maxsize
    total_water=0
    while q:
        r, c = q.popleft()
        pool.append((r, c))

        for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0>nr or nr>=N or 0>nc or nc>=M:
                return 0

            if not visited[nr][nc] and board[nr][nc]<=standard_height:
                visited[nr][nc] = True
                q.append((nr, nc))
            elif standard_height<board[nr][nc]:
                min_height=min(min_height,board[nr][nc])

    if min_height != sys.maxsize:
        for i in range(len(pool)):
            r,c=pool[i]
            total_water+=min_height-board[r][c]
            board[r][c]=min_height

    return total_water

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
answer = 0

for i in range(1, N - 1):
    for j in range(1, M - 1):
        answer+=bfs(i, j)

print(answer)