import sys

sys.setrecursionlimit(1000000)

N, M = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
answer = set()


def find(r, c, cycle_num):
    visited[r][c] = cycle_num
    nr, nc = r, c
    if board[r][c] == 'D':
        nr, nc = r + 1, c
    elif board[r][c] == 'L':
        nr, nc = r, c - 1
    elif board[r][c] == 'R':
        nr, nc = r, c + 1
    elif board[r][c] == 'U':
        nr, nc = r - 1, c

    if visited[nr][nc]:
        visited[r][c]=visited[nr][nc]
    else:
        visited[r][c]=find(nr, nc, cycle_num)
    return visited[r][c]


cycle_num=0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            cycle_num+=1
            answer.add(find(i, j,cycle_num))
print(len(answer))
