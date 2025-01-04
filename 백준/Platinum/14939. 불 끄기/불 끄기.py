import copy
import sys

def push(r,c,board):
    for dr,dc in (-1,0),(1,0),(0,-1),(0,1),(0,0):
        nr,nc=dr+r,dc+c
        if 0<=nr<10 and 0<=nc<10:
            board[nr][nc]=not board[nr][nc]

board=[list(sys.stdin.readline().rstrip()) for _ in range(10)]
for i in range(10):
    for j in range(10):
        if board[i][j]=='#':
            board[i][j]=0
        else:
            board[i][j]=1

answer=sys.maxsize
case=0

for _ in range(2**10):
    temp_board=copy.deepcopy(board)
    tmp=0
    for idx,st in enumerate(bin(case)[2:].zfill(10)):
        if st=='1':
            tmp+=1
            push(0,idx,temp_board)

    for i in range(1,10):
        for j in range(10):
            if temp_board[i-1][j]==1:
                push(i,j,temp_board)
                tmp+=1

    if all(i==0 for i in temp_board[9]):
        answer=min(tmp,answer)
    case+=1

print(answer if answer!=sys.maxsize else -1)