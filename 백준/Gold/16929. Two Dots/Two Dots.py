import sys

N,M=map(int,sys.stdin.readline().split())
dx=[0,0,-1,1]
dy=[1,-1,0,0]
board=[]
for _ in range(N):
    board.append(list(input()))

def dfs(start,r,c,visited,ex_y,ex_x):
    visited[r][c]=True

    for i in range(4):
        ny=r+dy[i]
        nx=c+dx[i]

        if ny<0 or nx<0 or ny>N-1 or nx>M-1:
            continue

        if board[ny][nx]==board[r][c]:

            if ny==start[0] and nx==start[1] and start[0]!=ex_y and start[1]!=ex_x:
                print('Yes')
                exit()

            if not visited[ny][nx]:
                dfs(start,ny,nx,visited,r,c)


for i in range(N):
    for j in range(M):
        visited = [[False for _ in range(M)] for _ in range(N)]
        dfs((i,j),i,j,visited,i,j)

print('No')
