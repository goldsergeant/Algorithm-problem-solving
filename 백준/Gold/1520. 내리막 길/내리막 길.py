import sys

m, n = map(int, sys.stdin.readline().split())
board = list(list(map(int, sys.stdin.readline().split())) for _ in range(m))
dp = [[-1 for _ in range(n)] for _ in range(m)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def dfs(row, col)->int:
    if row == m - 1 and col == n - 1:
        return 1
    if dp[row][col]!=-1:
        return dp[row][col]

    dp[row][col]=0

    for i in range(4):
        n_row = row + dy[i]
        n_col = col + dx[i]

        if n_row < 0 or n_col < 0 or n_row > m - 1 or n_col > n - 1:
            continue

        if board[n_row][n_col] < board[row][col]:
            dp[row][col]+=dfs(n_row,n_col)

    return dp[row][col]

dfs(0, 0)
print(dp[0][0])