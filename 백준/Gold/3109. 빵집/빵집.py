import collections
import sys

R, C = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
answer = 0
visited = [[False for _ in range(C)] for _ in range(R)]


def dfs(y, x):
    visited[y][x]=True

    if x==C-1:
        return True

    for dy, dx in (-1, 1), (0, 1), (1, 1),:
        ny, nx = y + dy, x + dx
        if 0 <= ny < R and 0 <= nx < C:
            if board[ny][nx]=='.' and not visited[ny][nx]:
                if dfs(ny,nx):
                    return True



for i in range(R):
    if dfs(i, 0):
        answer+=1
print(answer)
