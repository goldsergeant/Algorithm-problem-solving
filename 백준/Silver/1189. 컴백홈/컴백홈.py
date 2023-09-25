import sys

r, c, k = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().rstrip()) for _ in range(r)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
answer = 0
visited = [[False for _ in range(c)] for _ in range(r)]


def dfs(row, col, depth):
    global answer
    if row == 0 and col == c - 1 and depth == k:
        answer += 1
        return
    if depth >= k:
        return

    for i in range(4):
        n_row = row + dy[i]
        n_col = col + dx[i]
        if n_row < 0 or n_col < 0 or n_row > r - 1 or n_col > c - 1:
            continue
        if board[n_row][n_col] == 'T':
            continue
        if not visited[n_row][n_col]:
            visited[n_row][n_col] = True
            dfs(n_row, n_col, depth + 1)
            visited[n_row][n_col] = False


visited[r-1][0]=True
dfs(r - 1, 0, 1)
print(answer)
