import collections
import sys


def bfs():
    q = collections.deque()

    for i in range(N):
        for j in range(M):
            if bitmap[i][j] == '1':
                answer[i][j]=0
                q.append((i, j, i, j))

    while q:
        r, c, s_r, s_c = q.popleft()
        for dy, dx in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            nr, nc = dy + r, dx + c
            if 0 <= nr < N and 0 <= nc < M:
                if abs(nr-s_r)+abs(nc-s_c)<answer[nr][nc]:
                    answer[nr][nc]=abs(nr-s_r)+abs(nc-s_c)
                    q.append((nr, nc, s_r, s_c))


N, M = map(int, sys.stdin.readline().split())
bitmap = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
answer = [[sys.maxsize for _ in range(M)] for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

bfs()

for arr in answer:
    print(*arr)
