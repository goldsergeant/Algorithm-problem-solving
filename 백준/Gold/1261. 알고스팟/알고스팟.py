import collections
import sys

dy=[1,-1,0,0]
dx=[0,0,1,-1]

M,N=map(int,sys.stdin.readline().split())
miro=[]
for _ in range(N):
    miro.append(list(map(int,sys.stdin.readline().strip())))

def bfs():
    queue=collections.deque()
    visited=[[sys.maxsize for _ in range(M)] for _ in range(N)]
    queue.append((0,0,0))
    visited[0][0]=0

    while queue:
        temp=queue.popleft()
        row,col,break_count=temp[0],temp[1],temp[2]

        for i in range(4):
            ny=row+dy[i]
            nx=col+dx[i]

            if ny<0 or nx<0 or ny>N-1 or nx>M-1:
                continue

            if miro[ny][nx]==1:
                if break_count+1<visited[ny][nx]:
                    queue.append((ny,nx,break_count+1))
                    visited[ny][nx]=break_count+1
            elif miro[ny][nx]==0:
                if break_count<visited[ny][nx]:
                    queue.append((ny,nx,break_count))
                    visited[ny][nx]=break_count

    return visited[N-1][M-1]

print(bfs())