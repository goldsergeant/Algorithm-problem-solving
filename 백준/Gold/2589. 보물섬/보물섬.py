import collections
import sys

N,M=map(int,sys.stdin.readline().split())
board=[[*sys.stdin.readline().rstrip()] for _ in range(N)]
answer=0

q=collections.deque()

for i in range(N):
    for j in range(M):
        if board[i][j]=='L':
            q.append((i,j,0))
            visited=[[False for _ in range(M)] for _ in range(N)]
            visited[i][j]=True
            while q:
                r,c,d=q.popleft()
                answer=max(answer,d)
                for dy,dx in (-1,0),(1,0),(0,1),(0,-1),:
                    ny,nx=r+dy,c+dx
                    if 0<=ny<N and 0<=nx<M:
                        if not visited[ny][nx] and board[ny][nx]!='W':
                            visited[ny][nx]=True
                            q.append((ny,nx,d+1))

print(answer)