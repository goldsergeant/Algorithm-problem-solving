import collections
import sys

N,M=map(int,sys.stdin.readline().split())
Hx,Hy=map(int,sys.stdin.readline().split())
Ex,Ey=map(int,sys.stdin.readline().split())
board=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]

q=collections.deque([(Hx-1,Hy-1,1,0)])
visited=[[[False for _ in range(2)] for _ in range(M)] for _ in range(N)]
visited[Hx-1][Hy-1][1]=True

while q:
    x,y,has_chance,cnt=q.popleft()
    if (x,y)==(Ex-1,Ey-1):
        print(cnt)
        exit()

    for dx,dy in [(-1,0),(0,1),(1,0),(0,-1)]:
        nx,ny=x+dx,y+dy
        if 0<=nx<N and 0<=ny<M:
            if board[nx][ny]==0:
                if not visited[nx][ny][has_chance]:
                    visited[nx][ny][has_chance]=True
                    q.append((nx,ny,has_chance,cnt+1))
            else:
                if has_chance:
                    if not visited[nx][ny][0]:
                        visited[nx][ny][0]=True
                        q.append((nx,ny,0,cnt+1))
print(-1)