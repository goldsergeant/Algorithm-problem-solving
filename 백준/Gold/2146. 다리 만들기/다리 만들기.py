import collections
import sys
sys.setrecursionlimit(10**5)

dx=[0,0,1,-1]
dy=[1,-1,0,0]

N=int(input())
boards=[]
answer=[]
for _ in range(N):
    boards.append(list(map(int,sys.stdin.readline().split())))

def dfs(num,row,col):  # 섬에 따른 종류 표시
    if boards[row][col]!=1:
        return

    boards[row][col]=num

    for i in range(4):
        ny=row+dy[i]
        nx=col+dx[i]
        if ny<0 or ny>N-1 or nx<0 or nx>N-1 or boards[ny][nx]!=1:
            continue
        dfs(num,ny,nx)

def bfs(num,row,col):
    visited=[[False for _ in range(N)] for _ in range(N)]
    queue= collections.deque()
    queue.appendleft((row,col,1))
    visited[row][col]=True

    while queue:
        r,c,depth=queue.pop()
        if boards[r][c]!=num and boards[r][c]!=0:
            answer.append(depth-1)
            return

        for i in range(4):
            ny=r+dy[i]
            nx=c+dx[i]
            if ny<0 or ny>N-1 or nx<0 or nx>N-1:
                continue
            if not visited[ny][nx] and boards[ny][nx]!=num:
                visited[ny][nx]=True
                queue.appendleft((ny,nx,depth+1))
flag=2
for i in range(N):
    for j in range(N):
        if boards[i][j]==1:
            dfs(flag,i,j)
            flag+=1

for i in range(N):
    for j in range(N):
        if boards[i][j]!=0:
            for k in range(4):
                ny=i+dy[k]
                nx=j+dx[k]
                if ny < 0 or ny > N - 1 or nx < 0 or nx > N - 1:
                    continue
                if boards[ny][nx]==0:
                    bfs(boards[i][j],ny,nx)


print(min(answer))
