import collections
import sys

dir = [(0,1,0),(0,-1,0),(1,0,0),(-1,0,0),(0,0,-1),(0,0,1)]
vis=[False for _ in range(5)]
tops=[]
answer=sys.maxsize
def solve(depth):
    global answer
    if depth==5:
        # answer+=1
        if tops[0][0][0] and tops[4][4][4]:
            answer=min(answer,bfs())
        if answer==12:
            print(answer)
            exit()
        return

    for i in range(5):
        if not vis[i]:
            vis[i]=True
            for _ in range(4):
                rotate_board(i)
                tops.append(boards[i])
                solve(depth + 1)
                tops.pop()
            vis[i]=False


def bfs():
    q=collections.deque([(0,0,0,0)])
    visited=[[[False for _ in range(5)] for _ in range(5)] for _ in range(5)]
    visited[0][0][0]=True
    while q:
        x,y,z,cnt=q.popleft()
        if (x,y,z)==(4,4,4):
            return cnt

        for dx,dy,dz in dir:
            nx,ny,nz=x+dx,y+dy,z+dz
            if 0<=nx<5 and 0<=ny<5 and 0<=nz<5:
                if visited[nz][ny][nx]:
                    continue
                if tops[nz][ny][nx]==0:
                    continue
                visited[nz][ny][nx]=True
                q.append((nx,ny,nz,cnt+1))

    return sys.maxsize

boards=[]
def rotate_board(i):
    tmp_board=[[-1 for _ in range(5)] for _ in range(5)]
    for j in range(5):
        for k in range(5):
            tmp_board[j][k]=boards[i][5-k-1][j]

    boards[i]=tmp_board

for _ in range(5):
    boards.append([list(map(int,sys.stdin.readline().split())) for _ in range(5)])

solve(0)

print(answer if answer<sys.maxsize else -1)