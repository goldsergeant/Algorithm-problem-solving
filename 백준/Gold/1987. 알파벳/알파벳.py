import sys

r,c=map(int,sys.stdin.readline().split())
board=[sys.stdin.readline().rstrip() for _ in range(r)]
dy=[0,0,-1,1]
dx=[1,-1,0,0]
visited=[False for _ in range(26)]
answer=0
def dfs(row,col,depth):
    global answer
    answer=max(answer,depth)

    for i in range(4):
        n_row=row+dy[i]
        n_col=col+dx[i]
        if n_row<0 or n_col<0 or n_row>=r or n_col>=c:
            continue
        if not visited[ord(board[n_row][n_col])-65]:
            visited[ord(board[n_row][n_col])-65]=True
            dfs(n_row,n_col,depth+1)
            visited[ord(board[n_row][n_col])-65]=False

visited[ord(board[0][0])-65]=True
dfs(0,0,1)


print(answer)