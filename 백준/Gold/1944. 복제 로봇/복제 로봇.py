import collections
import sys
from heapq import heappop, heappush

N, M = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(N)]

distance = [[sys.maxsize for _ in range(N)] for _ in range(N)]

key_num = 0
s_r, s_c = 0, 0
for i in range(N):
    for j in range(N):
        if board[i][j] == 'S':
            s_r, s_c = i, j

heap = [(0, s_r, s_c)]
distance[s_r][s_c] = 0
has_key = set()
answer = 0
while heap:
    cnt, r, c = heappop(heap)
    if cnt>distance[r][c]:
        continue

    if board[r][c] == 'K' and (r,c) not in has_key:
        has_key.add((r,c))
        answer += cnt
        cnt = 0

        if len(has_key) == M:
            break

    for dr, dc in (0, -1), (0, 1), (1, 0), (-1, 0),:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < N:
            if board[nr][nc] != '1' and distance[nr][nc] > cnt + 1:
                if board[nr][nc]=='K' and (nr,nc) in has_key:
                    continue
                distance[nr][nc]=cnt+1
                heappush(heap, (cnt + 1, nr, nc))

print(answer if len(has_key)==M else -1)
