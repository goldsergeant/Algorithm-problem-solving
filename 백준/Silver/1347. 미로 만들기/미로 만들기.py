import sys

n = int(sys.stdin.readline())
directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]  # 남,서,북,동
note = sys.stdin.readline().rstrip()
board = [['#' for _ in range(110)] for _ in range(110)]
max_row=55
max_col=55
min_row=55
min_col=55
dir = 0
s_r=55
s_c=55
board[55][55]='.'
for char in note:
    if char == 'R':
        dir = (dir + 1) % 4
    elif char == 'L':
        dir -= 1
        if dir == -1:
            dir = 3
    elif char == 'F':
        s_r += directions[dir][0]
        s_c += directions[dir][1]
        board[s_r][s_c] = '.'
        min_row=min(min_row,s_r)
        min_col=min(min_col,s_c)
        max_row=max(max_row,s_r)
        max_col=max(max_col,s_c)

for i in range(min_row,max_row+1):
    for j in range(min_col,max_col+1):
        print(board[i][j],end='')
    print()