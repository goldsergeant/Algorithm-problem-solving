N=int(input())
find_num=int(input())
dy=[1,0,-1,0]
dx=[0,1,0,-1]
boards=[[0 for _ in range(N)] for _ in range(N)]
count=N*N
direction=-1
cur_row=0
cur_col=0
answer=[1,1]

boards[0][0]=count
count-=1
while True:

    n_row = cur_row + dy[direction]
    n_col = cur_col + dx[direction]
    if n_row < 0 or n_row > N - 1 or n_col < 0 or n_col > N - 1 or boards[n_row][n_col] != 0:
        direction = (direction + 1) % 4
        continue

    cur_row=n_row
    cur_col=n_col
    boards[cur_row][cur_col]=count
    if count==find_num:
        answer[0]=cur_row+1
        answer[1]=cur_col+1
    count-=1
    if cur_row==N//2 and cur_col==N//2:
        break

for board in boards:
    print(' '.join(map(str,board)))

print(*answer)