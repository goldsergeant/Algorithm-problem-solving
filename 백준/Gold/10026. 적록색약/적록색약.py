import collections
import sys
sys.setrecursionlimit(100000)

n = int(sys.stdin.readline())
board = list(list(sys.stdin.readline().rstrip()) for _ in range(n))
visited = [[False] * n for _ in range(n)]
dy=[-1,1,0,0]
dx=[0,0,-1,1]
answer_normal=0
answer_colorless=0

def dfs_normal(row,col):

    visited[row][col]=True

    for i in range(4):
        n_row=row+dy[i]
        n_col=col+dx[i]

        if n_row<0 or n_col<0 or n_row>n-1 or n_col>n-1:
            continue

        if board[n_row][n_col]==board[row][col] and not visited[n_row][n_col]:
            dfs_normal(n_row,n_col)

def dfs_colorless(row,col):

    visited[row][col]=True

    for i in range(4):
        n_row=row+dy[i]
        n_col=col+dx[i]

        if n_row<0 or n_col<0 or n_row>n-1 or n_col>n-1:
            continue

        if not visited[n_row][n_col]:
            if board[row][col]=='R' or board[row][col]=='G':
                if board[n_row][n_col]=='R' or board[n_row][n_col]=='G':
                    dfs_colorless(n_row,n_col)
            else:
                if board[row][col]==board[n_row][n_col]:
                    dfs_colorless(n_row,n_col)



for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            answer_normal+=1
            dfs_normal(i,j)

visited=[[False]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            answer_colorless+=1
            dfs_colorless(i,j)

print(answer_normal,answer_colorless)