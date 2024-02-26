import sys

M, N = map(int, sys.stdin.readline().split())
board = [[1 for _ in range(M)] for _ in range(M)]
for _ in range(N):
    arr = list(map(int, sys.stdin.readline().split()))
    row, col = M - 1, 0
    for i in range(len(arr)):
        while arr[i]>0:
            board[row][col] += i
            arr[i]-=1
            if row != 0:
                row -= 1
            else:
                col += 1

for i in range(1,M):
    for j in range(1,M):
        board[i][j]=max(board[i-1][j],board[i-1][j-1],board[i][j-1])

for arr in board:
    print(' '.join(map(str,arr)))