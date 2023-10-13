import sys
sys.setrecursionlimit(100000)

n,m,k=map(int,sys.stdin.readline().split())
board=[[0 for _ in range(m)] for _ in range(n)]
answer=0
dy=[-1,1,0,0]
dx=[0,0,-1,1]
for _ in range(k):
    row,col=map(int,sys.stdin.readline().split())
    board[row-1][col-1]=1

def dfs(row,col):
    result=1
    board[row][col]=0
    for i in range(4):
        n_row=dy[i]+row
        n_col=dx[i]+col
        if n_row<0 or n_col<0 or n_row>n-1 or n_col>m-1:
            continue
        if board[n_row][n_col]==1:
            result+=dfs(n_row,n_col)

    return result

for i in range(n):
    for j in range(m):
        if board[i][j]==1:
            answer=max(answer,dfs(i,j))

print(answer)
