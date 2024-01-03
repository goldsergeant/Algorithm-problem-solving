import collections
import sys
from heapq import heappop,heappush
H,W=map(int,sys.stdin.readline().split())
start,end=(0,0),(0,0)
board=[list(sys.stdin.readline().rstrip()) for _ in range(H)]
dy=[-1,1,0,0]
dx=[0,0,-1,1]

for i in range(H):
    for j in range(W):
        if board[i][j]=='S':
            start=(i,j)
        elif board[i][j]=='E':
            end=(i,j)

def is_adj_wall(row,col):
    for i in range(4):
        n_row=row+dy[i]
        n_col=col+dx[i]
        if 0<=n_row<H and 0<=n_col<W:
            if board[n_row][n_col]=='#':
                return True

    return False

def bfs():
    q=[(0,*start)]
    visited=[[False for _ in range(W)] for _ in range(H)]
    while q:
        time,row,col=heappop(q)
        if (row,col)==end:
            return time
        if not visited[row][col]:
            visited[row][col]=True
            for i in range(4):
                n_row=row+dy[i]
                n_col=col+dx[i]
                if 0<=n_row<H and 0<=n_col<W:
                    if board[n_row][n_col]!='#' and not visited[n_row][n_col]:
                        if is_adj_wall(row,col) and is_adj_wall(n_row,n_col):
                            heappush(q,(time,n_row,n_col))
                        else:
                            heappush(q,(time+1,n_row,n_col))


print(bfs())