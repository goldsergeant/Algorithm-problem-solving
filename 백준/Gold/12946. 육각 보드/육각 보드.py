import sys
sys.setrecursionlimit(100000+1)
dir=[(-1,0),(-1,1),(0,1),(1,0),(1,-1),(0,-1)]

def dfs(r,c,color):
    global answer
    answer=max(answer,1)
    visited[r][c]=color
    for dy,dx in dir:
        ny,nx=r+dy,c+dx
        if ny<0 or nx<0 or ny>=N or nx>=N:
            continue

        if board[ny][nx]=='X' and visited[ny][nx]==-1:
            dfs(ny,nx,1-color)
            answer=max(answer,2)
        if visited[ny][nx]==color:
            answer=3
            print(answer)
            exit()

N=int(sys.stdin.readline())
board=[list(sys.stdin.readline().rstrip()) for _ in range(N)]
visited=[[-1 for _ in range(N)] for _ in range(N)]
answer=0
for i in range(N):
     for j in range(N):
         if board[i][j]=='X' and visited[i][j]==-1:
             dfs(i,j,0)

print(answer)