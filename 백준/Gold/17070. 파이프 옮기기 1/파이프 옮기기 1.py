from collections import deque
import sys

n = int(input())
board = []
dp = [[[0 for _ in range(3)] for _ in range(n)] for _ in range(n)]  # dp[row][col][direct] 0 가 1 세 2 대
for _ in range(n):
    board.append([int(x) for x in sys.stdin.readline().rstrip().split()])

dp[0][1][0] = 1
for i in range(2, n):
    if board[0][i] == 0:
        dp[0][i][0] = dp[0][i - 1][0]

for row in range(1,n):
    for col in range(1,n):
        if board[row][col]==0:
            dp[row][col][0]=dp[row][col-1][0]+dp[row][col-1][2] # 가로
            dp[row][col][1]=dp[row-1][col][1]+dp[row-1][col][2] # 세로

            if board[row][col-1]==0 and board[row-1][col]==0: # 대각선
                dp[row][col][2]=sum(i for i in dp[row-1][col-1])


print(sum(i for i in dp[n-1][n-1]))





