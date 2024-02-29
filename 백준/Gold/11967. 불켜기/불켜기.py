import collections
import sys

N, M = map(int, sys.stdin.readline().split())
board = [[set() for _ in range(N)] for _ in range(N)]

for _ in range(M):
    x, y, a, b = map(int, sys.stdin.readline().split())
    board[x - 1][y - 1].add((a - 1, b - 1))

q = collections.deque([(0, 0)])
lights={(0,0)}
visited = [[False for _ in range(N)] for _ in range(N)]

while q:
    r, c = q.popleft()
    for y,x in board[r][c]:
        if (y,x) not in lights:
            lights.update(board[r][c])
            q.clear()
            visited=[[False for _ in range(N)] for _ in range(N)]
            visited[r][c]=True
            break

    for dy, dx in (-1, 0), (1, 0), (0, -1), (0, 1),:
        nr, nc = r + dy, c + dx

        if 0 <= nr < N and 0 <= nc < N:
            if not visited[nr][nc] and (nr, nc) in lights:
                visited[nr][nc] = True
                q.append((nr, nc))

print(len(lights))
