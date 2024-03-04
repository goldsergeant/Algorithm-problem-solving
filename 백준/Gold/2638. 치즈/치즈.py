import collections
import sys

N,M=map(int,sys.stdin.readline().split())
dy=[-1,0,1,0]
dx=[0,-1,0,1]
board=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
OUT_SPACE=-1
IN_SPACE=0
CHEESE=1

def check_space():
    q=collections.deque([(0,0)])
    visited=[[False for _ in range(M)] for _ in range(N)]
    visited[0][0]=True
    while q:
        y,x=q.popleft()
        board[y][x]=OUT_SPACE
        for i in range(4):
            ny=y+dy[i]
            nx=x+dx[i]
            if 0<=ny<N and 0<=nx<M:
                if not visited[ny][nx] and (board[ny][nx]==OUT_SPACE or board[ny][nx]==IN_SPACE):
                    visited[ny][nx]=True
                    q.append((ny,nx))

def melt_cheese():
    cheeses=[]
    for i in range(N):
        for j in range(M):
            if board[i][j]==CHEESE:
                out_space_cnt=0
                for k in range(4):
                    ny,nx=i+dy[k],j+dx[k],
                    if 0<=ny<N and 0<=nx<M:
                        if board[ny][nx]==OUT_SPACE:
                            out_space_cnt+=1

                if out_space_cnt>=2:
                    cheeses.append((i,j))

    for r,c in cheeses:
        board[r][c]=OUT_SPACE

def is_all_removed():
    for i in range(N):
        for j in range(M):
            if board[i][j]==CHEESE:
                return False

    return True

time=0
while True:
    if is_all_removed():
        break

    time+=1
    check_space()
    melt_cheese()

print(time)