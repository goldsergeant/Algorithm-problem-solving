import sys

n, m = map(int, input().split())
r, c, d = map(int, input().split())  # 0 북, 1 동, 2 남, 3 서
dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]
board = []
answer = 0


def rotate():
    global d
    d -= 1
    if d == -1:
        d = 3


def can_move_forward():
    global r, c, d, answer
    if d == 0:
        if board[r - 1][c] == 0:
            r -= 1
            return True

    elif d == 1:
        if board[r][c + 1] == 0:
            c += 1
            return True
    elif d == 2:
        if board[r + 1][c] == 0:
            r += 1
            return True
    elif d == 3:
        if board[r][c - 1] == 0:
            c -= 1
            return True

    return False


def can_move_backward():
    global r, c, d, answer
    if d == 0:
        if board[r + 1][c] == 1:
            return False
        else:
            r += 1
    elif d == 1:
        if board[r][c - 1] == 1:
            return False
        else:
            c -= 1
    elif d == 2:
        if board[r - 1][c] == 1:
            return False
        else:
            r -= 1
    elif d == 3:
        if board[r][c + 1] == 1:
            return False
        else:
            c += 1

    return True


for _ in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    board.append(tmp)

while True:
    flag=0
    if board[r][c] == 0:
        board[r][c] = 2
        answer += 1

    for i in range(4):
        ny = r + dy[i]
        nx = c + dx[i]

        if board[ny][nx] == 0:  # 주변 4칸 중 청소되지 않은 빈칸이 있는 경우
            flag=1
            rotate()
            if can_move_forward():
                break

    if flag==0:
        # 빈칸이 없는 경우
        if can_move_backward():
            continue
        else:
            print(answer)
            exit()
