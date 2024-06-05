import sys

def get_total(left_row, left_col, right_row, right_col):
    left_row,left_col,right_row,right_col=left_row+1,left_col+1,right_row+1,right_col+1
    total=t_sum[right_row][right_col]-t_sum[right_row][left_col-1]-t_sum[left_row-1][right_col]+t_sum[left_row-1][left_col-1]
    return total

N,M=map(int,sys.stdin.readline().split())
board=[list(map(int,sys.stdin.readline().rstrip())) for _ in range(N)]
answer=0
t_sum=[[0 for _ in range(M+1)] for _ in range(N+1)]

t_sum[1][1]=board[0][0]
for j in range(1,M):
    t_sum[1][j+1]=t_sum[1][j-1+1]+board[0][j]
for i in range(1,N):
    t_sum[i+1][1]=t_sum[i-1+1][1]+board[i][0]
    for j in range(1,M):
        t_sum[i+1][j+1]=t_sum[i+1][j-1+1]+t_sum[i-1+1][j+1]+board[i][j]-t_sum[i-1+1][j-1+1]

for i1 in range(N-2):
    for i2 in range(i1+1,N-1):
        square1=get_total(0,0,i1,M-1)
        square2=get_total(i1+1,0,i2,M-1)
        square3=get_total(i2+1,0,N-1,M-1)
        answer=max(answer, square1*square2*square3)

for j1 in range(M-2):
    for j2 in range(j1+1,M-1):
        square1=get_total(0,0,N-1,j1)
        square2=get_total(0,j1+1,N-1,j2)
        square3=get_total(0,j2+1,N-1,M-1)
        answer=max(answer, square1*square2*square3)

for j in range(1,M):
    for i in range(N-1):
        square1=get_total(0,0,i,j)
        square2=get_total(i+1,0,N-1,j)
        square3=get_total(0,j+1,N-1,M-1)
        answer=max(answer,square1*square2*square3)

for j in range(M-1):
    for i in range(N-1):
        square1=get_total(0,0,N-1,j)
        square2=get_total(0,j+1,i,M-1)
        square3=get_total(i+1,j+1,N-1,M-1)
        answer=max(answer,square1*square2*square3)

for i in range(N-1):
    for j in range(M-1):
        square1=get_total(0,0,i,M-1)
        square2=get_total(i+1,0,N-1,j)
        square3=get_total(i+1,j+1,N-1,M-1)
        answer=max(answer,square1*square2*square3)

for i in range(N-1):
    for j in range(M-1):
        square1=get_total(0,0,i,j)
        square2=get_total(0,j+1,i,M-1)
        square3=get_total(i+1,0,N-1,M-1)
        answer=max(answer,square1*square2*square3)

print(answer)