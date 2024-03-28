import collections
import sys

board = [list(sys.stdin.readline().rstrip()) for _ in range(8)]
dr = [0, 0, 1, -1, 1, -1, 1, -1, 0]
dc = [1, -1, 0, 0, 1, 1, -1, -1, 0]

def move_blocks():
    board.pop()
    board.insert(0,['.' for _ in range(8)])
def bfs():
    q = collections.deque([(7, 0)])
    second = 0
    while q:
        for _ in range(len(q)):
            r, c = q.popleft()
            if board[r][c]=='#':
                continue
            if r == 0 or second == 9:
                return 1

            for i in range(len(dr)):
                nr, nc = dr[i] + r, dc[i] + c
                if 0 <= nr < 8 and 0 <= nc < 8:
                    if board[nr][nc]!='#':
                        q.append((nr, nc))
        move_blocks()
        second += 1
    return 0


print(bfs())