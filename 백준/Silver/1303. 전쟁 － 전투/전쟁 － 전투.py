import sys

dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]
answer = [0,0]


def dfs(row, col, word):
    global cnt
    cnt+=1
    board[row][col]='.'
    for i in range(4):
        n_row = row + dy[i]
        n_col = col + dx[i]
        if n_row < 0 or n_col < 0 or n_row > m - 1 or n_col > n - 1:
            continue
        if board[n_row][n_col] == word:
            dfs(n_row, n_col, word)


n, m = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(m)]

for i in range(m):
    for j in range(n):
        cnt=0
        if board[i][j] != '.':
            word=board[i][j]
            dfs(i, j, board[i][j])
            if word=='W':
                answer[0]+=cnt**2
            else:
                answer[1]+=cnt**2

print(*answer)
