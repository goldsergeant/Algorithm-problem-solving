import collections
import sys

n,m,h=map(int,sys.stdin.readline().split())
board=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
answer=0
target_row,target_col=0,0
mints=[]


for i in range(n):
    for j in range(n):
        if board[i][j]==1:
            target_row,target_col=i,j
        elif board[i][j]==2:
            mints.append((i,j))

def dfs(cur_row,cur_col,health,mint):
    global answer

    if abs(cur_row-target_row)+abs(cur_col-target_col)<=health:
        answer=max(answer,mint)

    for row,col in mints:
        if board[row][col]==2:
            distance=abs(row-cur_row)+abs(col-cur_col)
            if health>=distance:
                board[row][col]=0
                dfs(row,col,health+h-distance,mint+1)
                board[row][col]=2

dfs(target_row,target_col,m,0)
print(answer)