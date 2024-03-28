import collections
import sys

board = [list(sys.stdin.readline().rstrip()) for _ in range(8)]
dr = [0, 0, 1, -1, 1, -1, 1, -1, 0]
dc = [1, -1, 0, 0, 1, 1, -1, -1, 0]
blocks = []
for i in range(8):
    for j in range(8):
        if board[i][j] == '#':
            blocks.append((i, j))


def move_blocks():
    for i in range(len(blocks)):
        r, c = blocks[i]
        blocks[i]=(r+1,c)
def bfs():
    q = collections.deque([(7, 0)])
    second = 0
    while q:
        for _ in range(len(q)):
            r, c = q.popleft()
            if (r,c) in blocks:
                continue
            if r == 0 or second == 9:
                return 1

            for i in range(len(dr)):
                nr, nc = dr[i] + r, dc[i] + c
                if 0 <= nr < 8 and 0 <= nc < 8:
                    if (nr,nc) not in blocks:
                        q.append((nr, nc))
        move_blocks()
        second += 1
    return 0


print(bfs())