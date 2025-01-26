import sys
from functools import cache
sys.setrecursionlimit(1000000)

N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = 0


@cache
def dfs(r, c):
    cnt = 1

    for dr, dc in ((0, 1), (1, 0), (-1, 0), (0, -1)):
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < N:
            if board[nr][nc] > board[r][c]:
                cnt = max(cnt, dfs(nr, nc) + 1)

    return cnt


for i in range(N):
    for j in range(N):
        answer = max(answer, dfs(i, j))

print(answer)
