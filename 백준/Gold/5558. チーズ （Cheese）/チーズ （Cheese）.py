import collections
import sys

H, W, N = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(H)]


def bfs(s_r, s_c):
    visited = [[False for _ in range(W)] for _ in range(H)]
    q = collections.deque([(s_r, s_c, 0, 1)])
    visited[s_r][s_c] = True

    while q:
        y, x, step, health = q.popleft()
        if health > N:
            return step
        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < H and 0 <= nx < W:
                if board[ny][nx] != 'X' and not visited[ny][nx]:
                    if board[ny][nx].isdigit() and health >= int(board[ny][nx]):
                        q.clear()
                        visited = [[False for _ in range(W)] for _ in range(H)]
                        visited[ny][nx] = True
                        board[ny][nx] = '.'
                        q.append((ny, nx, step + 1, health + 1))
                        break
                    else:
                        visited[ny][nx]=True
                        q.append((ny,nx,step+1,health))

for i in range(H):
    for j in range(W):
        if board[i][j] == 'S':
            print(bfs(i, j))
            sys.exit()
