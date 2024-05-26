import sys
from collections import deque

N,K=map(int,sys.stdin.readline().split())
board=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
S,Y,X=map(int,sys.stdin.readline().split())
Y-=1
X-=1
points=[]
for i in range(N):
    for j in range(N):
        if board[i][j]!=0:
            points.append((i,j))

points.sort(key=lambda x:board[x[0]][x[1]])

q=deque(points)

for _ in range(S):
    for _ in range(len(q)):
        r,c=q.popleft()
        num=board[r][c]
        if r==Y and c==X:
            break

        for dr,dc in [(-1,0),(0,1),(1,0),(0,-1)]:
            nr,nc=r+dr,c+dc
            if 0<=nr<N and 0<=nc<N and board[nr][nc]==0:
                board[nr][nc]=num
                q.append((nr,nc))


print(board[Y][X])
