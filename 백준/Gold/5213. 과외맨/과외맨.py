import collections
import sys

def bfs():
    global answer
    q = collections.deque()
    q.append((1, [1]))
    visited = [sys.maxsize] + [sys.maxsize for _ in range(N * N - N // 2)]
    visited[1] = 1
    last_tile=0

    while q:
        tile, path = q.popleft()
        if tile>last_tile:
            answer = path
            last_tile=tile

        elif tile==last_tile:
            if len(answer) > len(path):
                answer=path

        if tile==target:
            continue

        r1,c1,r2,c2=tile_points[tile]

        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr1, nc1 = r1 + dr, c1 + dc
            nr2, nc2 = r2 + dr, c2 + dc


            if 0 <= nr1 < N and 0 <= nc1 < N*2:
                ntile1 = board_number[nr1][nc1]
                if board[r1][c1]==board[nr1][nc1] and len(path)+1<visited[ntile1]:
                    visited[ntile1]=len(path)+1
                    q.append((ntile1,path+[ntile1]))

            if 0 <= nr2 < N and 0 <= nc2 < N*2:
                ntile2 = board_number[nr2][nc2]
                if board[r2][c2]==board[nr2][nc2] and len(path)+1<visited[ntile2]:
                    visited[ntile2]=len(path)+1
                    q.append((ntile2,path+[ntile2]))

N = int(sys.stdin.readline())
board_number = [[0 for _ in range(N * 2)] for _ in range(N)]
board = [[0 for _ in range(N * 2)] for _ in range(N)]
tile_points = [(0, 0, 0, 0)] + [(0, 0, 0, 0) for _ in range(N * N - N // 2)]
tiles = [(0, 0)] + [list(map(int, sys.stdin.readline().split())) for _ in range(N * N - N // 2)]
answer = []
r, c = 0, 0
target = 0
for number, tile in enumerate(tiles):
    if number == 0:
        continue

    a, b = tile
    board[r][c] = a
    board[r][c + 1] = b
    tile_points[number] = (r,c,r,c+1)
    board_number[r][c] = number
    board_number[r][c + 1] = number
    target = max(number, target)

    if r % 2 == 0:
        if c + 1 == 2 * N - 1:
            r += 1
            c = 1
        else:
            c += 2
    else:
        if c + 1 == 2 * N - 2:
            r += 1
            c = 0
        else:
            c += 2


bfs()
# for arr in board:
#     print(arr)
# print()
# for arr in board_number:
#     print(arr)
print(len(answer))
print(*answer)