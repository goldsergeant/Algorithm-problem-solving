import collections
import sys

N,M=map(int,sys.stdin.readline().split())
board=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
year=0
dy=(0,0,-1,1)
dx=(-1,1,0,0)
def melt():
    adj_see=[[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j]!=0:
                for k in range(4):
                    ny = dy[k] + i
                    nx = dx[k] + j
                    if 0 <= ny < N and 0 <= nx < M:
                        if board[ny][nx]==0:
                            adj_see[i][j]+=1

    for i in range(N):
        for j in range(M):
            if adj_see[i][j]>0:
                board[i][j]=max(board[i][j]-adj_see[i][j],0)
def bfs(row,col):
    visited[row][col]=True
    q=collections.deque([(row,col)])

    while q:
        y,x=q.popleft()
        for i in range(4):
            ny = dy[i] + y
            nx = dx[i] + x
            if 0 <= ny < N and 0 <= nx < M:
                if board[ny][nx]!=0 and not visited[ny][nx]:
                    visited[ny][nx]=True
                    q.append((ny,nx))

while True:
    visited=[[False for _ in range(M)] for _ in range(N)]
    ice_cnt=0
    for i in range(N):
        for j in range(M):
            if board[i][j]!=0 and not visited[i][j]:
                bfs(i,j)
                ice_cnt+=1

    if ice_cnt>=2:
        break
    elif ice_cnt==0:
        year=0
        break

    melt()
    year+=1


print(year)
