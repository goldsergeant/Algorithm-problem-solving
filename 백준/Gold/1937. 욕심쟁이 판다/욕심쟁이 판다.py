import sys
sys.setrecursionlimit(100000)
n=int(sys.stdin.readline())
board=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
dy=[-1,1,0,0]
dx=[0,0,-1,1]
dp=[[0 for _ in range(n)] for _ in range(n)]

def dfs(row,col):
    if dp[row][col]!=0:
        return dp[row][col]

    tmp=0
    for i in range(4):
        n_row=row+dy[i]
        n_col=col+dx[i]
        if n_row<0 or n_col<0 or n_row>n-1 or n_col>n-1:
            continue
        if board[row][col]<board[n_row][n_col]:
            tmp=max(tmp,dfs(n_row,n_col))

    dp[row][col]=tmp+1
    return dp[row][col]

for i in range(n):
    for j in range(n):
        if dp[i][j]==0:
            dfs(i,j)

print(max(max(arr) for arr in dp))