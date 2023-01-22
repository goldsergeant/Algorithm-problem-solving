import sys

board = []
for i in range(9):
    board.append(list(map(int, sys.stdin.readline().split())))


def checkBoard(i, j,num):
    for index in range(9):
        if index!=j and board[i][index]==num:
            return False
        if index!=i and board[index][j]==num:
            return False

    j = j // 3 * 3
    i = i // 3 * 3
    for y in range(3):
        for x in range(3):
            if board[i + y][j+x] == num:
                return False

    return True


def dfs(depth):
    if depth == len(zero):
        printBoard()
        exit(0)

    y=zero[depth][0]
    x=zero[depth][1]
    for num in range(1,10):
        if checkBoard(y,x,num):
            board[y][x]=num
            dfs(depth+1)
            board[y][x]=0

def printBoard():
    for i in range(9):
        print(' '.join(map(str, board[i])))

zero = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            zero.append([i, j])
dfs(0)
