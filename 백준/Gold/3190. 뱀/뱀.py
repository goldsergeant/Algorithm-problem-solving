import collections
import sys

n = int(input())
board = [[0 for _ in range(n)] for _ in range(n)]  # 평소는 0, 뱀은 1, 사과는 2
direction = [(0,1),(1,0),(0,-1),(-1,0)]  # 우하좌상
snake=collections.deque()
snake.append((0,0))
head = 0
board[0][0] = 1
cur_row = 0
cur_col = 0
k = int(input())
move_info = collections.deque()
second=0
for _ in range(k):
    r, c = map(int, sys.stdin.readline().split())
    board[r - 1][c - 1] = 2

l = int(input())
for _ in range(l):
    x, c = sys.stdin.readline().split()
    x = int(x)
    move_info.append((x, c))

while True:
    n_row = cur_row + direction[head][0]
    n_col=cur_col+direction[head][1]
    second+=1
    if n_row<0 or n_col<0 or n_row>n-1 or n_col>n-1 or board[n_row][n_col]==1:
        break

    cur_row=n_row
    cur_col=n_col
    snake.append((cur_row,cur_col))
    if board[cur_row][cur_col]==0:
        r,c=snake.popleft()
        board[r][c]=0
    board[cur_row][cur_col]=1

    if move_info and second==move_info[0][0]:
        turn=move_info.popleft()[1]
        if turn=='L':
            head-=1
            if head==-1:
                head=3
        elif turn=='D':
            head=(head+1)%4

print(second)