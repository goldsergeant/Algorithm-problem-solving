import sys

N,M=map(int,sys.stdin.readline().split())
dx=[0,0,-1,1]
dy=[1,-1,0,0]
board=[]
for _ in range(N):
    board.append(list(input()))

def dfs(start,r,c,depth):

    for i in range(4):
        ny=r+dy[i]
        nx=c+dx[i]

        if ny<0 or nx<0 or ny>N-1 or nx>M-1:
            continue

        if board[ny][nx]==board[r][c]:

            if ny==start[0] and nx==start[1] and depth>=4:
                print('Yes')
                exit()

            if not visited[ny][nx]:
                visited[ny][nx]=True
                dfs(start,ny,nx,depth+1)
                visited[ny][nx]=False

visited = [[False for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        visited[i][j]=True
        dfs((i,j),i,j,1)
        visited[i][j]=False

print('No')
