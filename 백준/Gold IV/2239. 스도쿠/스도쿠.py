import sys

d_p = [(0, 1, 2), (-1, 0, 1), (0, -1, -1)]

board = []
zero_points = []
for i in range(9):
    arr = list(map(int, sys.stdin.readline().rstrip()))
    for j in range(9):
        if arr[j] == 0:
            zero_points.append((i, j))
    board.append(arr)


# 행 체크
def row_check(r, num):
    for c in range(9):
        if board[r][c] == num:
            return False
    return True

# 열 체크
def col_check(c, num):
    for r in range(9):
        if board[r][c] == num:
            return False
    return True

# 3 * 3 체크
def square_check(r, c, num):
    nc = (c // 3) * 3
    nr = (r // 3) * 3
    for x in range(3):
        for y in range(3):
            if board[nr + x][nc + y] == num:
                return False
    return True


def dfs(depth):
    if depth >= len(zero_points):  # 만약 0의 개수에 도달 했다면
        for k in range(9):
            print(''.join(map(str, board[k])))
        exit()

    r, c = zero_points[depth]  # 0의 좌표를 dfs를 돈다.
    for num in range(1, 9 + 1):
        if row_check(r, num) and col_check(c,num) and square_check(r,c,num):
            board[r][c] = num
            dfs(depth + 1)
            board[r][c] = 0


dfs(0)