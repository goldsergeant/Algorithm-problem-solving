import sys

n, m, k = map(int, sys.stdin.readline().split())
board = []
sum_white = [[0 for i in range(m + 1)] for i in range(n + 1)]
sum_black = [[0 for i in range(m + 1)] for i in range(n + 1)]
answer = sys.maxsize
for _ in range(n):
    board.append(sys.stdin.readline().strip())

for i in range(n):
    for j in range(m):
        if (i + j) % 2 == 0:
            if board[i][j] == 'B':
                sum_white[i + 1][j + 1] = sum_white[i + 1][j] + sum_white[i][j + 1] - sum_white[i][j]+1
                sum_black[i + 1][j + 1] = sum_black[i + 1][j] + sum_black[i][j + 1] - sum_black[i][j]
            elif board[i][j] == 'W':
                sum_white[i + 1][j + 1] = sum_white[i + 1][j] + sum_white[i][j + 1] - sum_white[i][j]
                sum_black[i + 1][j + 1] = sum_black[i + 1][j] + sum_black[i][j + 1] - sum_black[i][j]+1
        elif (i + j) % 2 == 1:
            if board[i][j] == 'B':
                sum_white[i + 1][j + 1] = sum_white[i + 1][j] + sum_white[i][j + 1] - sum_white[i][j]
                sum_black[i + 1][j + 1] = sum_black[i + 1][j] + sum_black[i][j + 1] - sum_black[i][j]+1
            elif board[i][j] == 'W':
                sum_white[i + 1][j + 1] = sum_white[i + 1][j] + sum_white[i][j + 1] - sum_white[i][j]+1
                sum_black[i + 1][j + 1] = sum_black[i + 1][j] + sum_black[i][j + 1] - sum_black[i][j]

for i in range(1, n - k + 2):
    for j in range(1, m - k + 2):
        b = sum_black[i + k - 1][j + k - 1] - sum_black[i + k - 1][j - 1] - sum_black[i - 1][j + k - 1] + \
            sum_black[i - 1][j - 1]
        w = sum_white[i + k - 1][j + k - 1] - sum_white[i + k - 1][j - 1] - sum_white[i - 1][j + k - 1] + \
            sum_white[i - 1][j - 1]
        answer = min(answer, b, w)

print(answer)

