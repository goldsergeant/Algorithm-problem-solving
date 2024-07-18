import collections
import sys

N, M = map(int, sys.stdin.readline().split())
Tg, Tb, X, Bp = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
q = collections.deque()
tmp_q = collections.deque()
visited = [[sys.maxsize for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if board[i][j] == '*':
            q.append((i, j, 0))
            visited[i][j] = 0

for cur in range(1, Tg + 1):
    for _ in range(len(q)):
        i, j, t = q.popleft()

        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny, nx = i + dy, j + dx
            if ny < 0 or ny >= N or nx < 0 or nx >= M:
                continue
            if visited[ny][nx] > cur:
                visited[ny][nx] = cur
                if board[ny][nx] != '#':
                    q.append((ny, nx, cur))
                else:
                    tmp_q.append((ny, nx, cur))

    while tmp_q and cur - tmp_q[0][2] + 1 > Tb:
        q.appendleft(tmp_q.popleft())

answer = []
for i in range(N):
    for j in range(M):
        if board[i][j] == '#':
            if visited[i][j] + Tb > Tg:
                answer.append((i, j))
        else:
            if visited[i][j] == sys.maxsize:
                answer.append((i, j))

if not answer:
    print(-1)
else:
    for i, j in answer:
        print(i + 1, j + 1)
