import sys

HORIZONTAL = 0
VERTICAL = 1
DIAGONAL = 2

N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[[0 for _ in range(3)] for _ in range(N)] for _ in range(N)]
dp[0][1][HORIZONTAL] = 1

for j in range(2, N):
    if board[0][j] == 1:
        break
    dp[0][j][HORIZONTAL] = 1

for i in range(1, N):
    for j in range(2, N):
        if board[i][j] == 1:
            continue

        if board[i][j - 1] == 0:
            dp[i][j][HORIZONTAL] = dp[i][j - 1][HORIZONTAL] + dp[i][j - 1][DIAGONAL]

        if board[i - 1][j] == 0:
            dp[i][j][VERTICAL] = dp[i - 1][j][VERTICAL] + dp[i - 1][j][DIAGONAL]

        if board[i - 1][j] == 0 and board[i][j - 1] == 0 and board[i - 1][j - 1] == 0:
            dp[i][j][DIAGONAL] = dp[i - 1][j - 1][HORIZONTAL] + dp[i - 1][j - 1][VERTICAL]+dp[i-1][j-1][DIAGONAL]

print(sum(dp[N-1][N-1]))