import collections
import sys

N=int(sys.stdin.readline())
board=[list(sys.stdin.readline().rstrip()) for _ in range(N)]
answer=sys.maxsize
dy=[-1,0,1,0]
dx=[0,-1,0,1]
q=collections.deque()
end=tuple()

for i in range(N):
    for j in range(N):
        if board[i][j]=='#':
            if len(q)==0:
                for k in range(4):
                    ni,nj=i+dy[k],j+dx[k]
                    if 0<=ni<N and 0<=nj<N:
                        if board[ni][nj]!='*':
                            q.append((i,j,0,k))
            else:
                end=(i,j)

visited=[[[sys.maxsize for _ in range(4)] for _ in range(N)] for _ in range(N)]
while q:
    y,x,break_cnt,dir=q.popleft()

    if y==end[0] and x==end[1]:
        answer=min(answer,break_cnt)
        continue


    ny,nx=y+dy[dir],x+dx[dir]
    if 0<=ny<N and 0<=nx<N:
        if visited[ny][nx][dir]>break_cnt and board[ny][nx]!='*':
            visited[ny][nx][dir]=break_cnt
            q.appendleft((ny,nx,break_cnt,dir))

    if board[y][x]=='!':
        if dir==0 or dir==2:
            ny,nx=y+dy[1],x+dx[1]
            if 0<=ny<N and 0<=nx<N:
                if visited[ny][nx][1]>break_cnt+1 and board[ny][nx]!='*':
                    visited[ny][nx][1]=break_cnt+1
                    q.append((ny,nx,break_cnt+1,1))
            ny, nx = y + dy[3], x + dx[3]
            if 0 <= ny < N and 0 <= nx < N:
                if visited[ny][nx][3]>break_cnt+1 and board[ny][nx] != '*':
                    visited[ny][nx][3]=break_cnt+1
                    q.append((ny, nx,break_cnt+1,3))
        else:
            ny, nx = y + dy[0], x + dx[0]
            if 0 <= ny < N and 0 <= nx < N:
                if visited[ny][nx][0]>break_cnt+1 and board[ny][nx] != '*':
                    visited[ny][nx][0]=break_cnt+1
                    q.append((ny, nx,break_cnt+1,0))
            ny, nx = y + dy[2], x + dx[2]
            if 0 <= ny < N and 0 <= nx < N:
                if visited[ny][nx][2]>break_cnt+1 and board[ny][nx] != '*':
                    visited[ny][nx][2]=break_cnt+1
                    q.append((ny, nx,break_cnt+1,2))


print(answer)
