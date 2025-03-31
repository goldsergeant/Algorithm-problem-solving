import collections
import sys

dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
N, M = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(N)]
field_to_gift_num = dict()
gift_num = 0
q = collections.deque()
for i in range(N):
    for j in range(M):
        if board[i][j] == 'C':
            field_to_gift_num[(i, j)] = gift_num
            gift_num += 1
        elif board[i][j] == 'S':
            q.append((i, j, -1, 0, 0))

visited = [[[[False for _ in range(1 << gift_num)] for _ in range(5)] for _ in range(M)] for _ in
           range(N)]  # r,c,dir,bit
visited[q[0][0]][q[0][1]][4][0] = True
all_bit = 0
for i in range(gift_num):
    all_bit = all_bit | (1 << i)

while q:
    r, c, d, bit, move_cnt = q.popleft()

    if bit==all_bit:
        print(move_cnt)
        exit()
    for i in range(4):
        if i == d:  # 같은 방향으로 두 번 이동 불가
            continue
        nr, nc = r + dir[i][0], c + dir[i][1]

        if nr<0 or nc<0 or nr>=N or nc>=M:
            continue

        if board[nr][nc] == '#':
            continue

        if board[nr][nc] == 'C':
            if bit & (1 << field_to_gift_num[(nr, nc)]):
                continue
            next_bit=bit | (1<<field_to_gift_num[(nr,nc)])
            if not visited[nr][nc][i][next_bit]:
                visited[nr][nc][i][next_bit] = True
                q.append((nr,nc,i,next_bit,move_cnt+1))

        else:
            if not visited[nr][nc][i][bit]:
                visited[nr][nc][i][bit] = True
                q.append((nr, nc, i, bit, move_cnt + 1))
print(-1)