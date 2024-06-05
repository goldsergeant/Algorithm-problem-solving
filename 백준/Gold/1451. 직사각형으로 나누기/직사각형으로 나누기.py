import sys

def get_total(left_row, left_col, right_row, right_col):
    total=0
    for i in range(left_row, right_row + 1):
        for j in range(left_col, right_col + 1):
            total+=board[i][j]
    return total

N,M=map(int,sys.stdin.readline().split())
board=[list(map(int,sys.stdin.readline().rstrip())) for _ in range(N)]
answer=0

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
# t_sum=[[0 for _ in range(M)] for _ in range(N)]
#
# t_sum[0][0]=board[0][0]
# for j in range(1,M):
#     t_sum[0][j]=t_sum[0][j-1]+board[0][j]
# for i in range(1,N):
#     t_sum[i][0]=t_sum[i-1][0]+board[i][0]
#     for j in range(1,M):
#         t_sum[i][j]=t_sum[i][j-1]+t_sum[i-1][j]+board[i][j]-t_sum[i-1][j-1]
