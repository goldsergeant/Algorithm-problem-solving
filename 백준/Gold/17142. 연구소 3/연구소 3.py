import collections
import itertools
import sys
from itertools import combinations

def bfs(virus_points):
    q=collections.deque()
    visited=[[sys.maxsize for _ in range(N)] for _ in range(N)]
    for y,x in virus_points:
        q.append((y,x,0))
        visited[y][x]=0

    while q:
        y,x,second=q.popleft()
        for dy,dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny,nx=y+dy,x+dx
            if 0<=ny<N and 0<=nx<N:
                if second+1<visited[ny][nx] and board[ny][nx]!=BLOCK:
                    visited[ny][nx]=second+1
                    q.append((ny,nx,second+1))

    total_duration=0
    for i in range(N):
        for j in range(N):
            if board[i][j]==EMPTY:
                total_duration=max(total_duration,visited[i][j])

    return total_duration

EMPTY=0
BLOCK=1
VIRUS=2
N,M=map(int,sys.stdin.readline().split())
board=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
answer=sys.maxsize

all_virus_points=[]
for i in range(N):
    for j in range(N):
        if board[i][j]==VIRUS:
            all_virus_points.append((i,j))

for virus_points in combinations(all_virus_points,M):
    answer=min(answer,bfs(virus_points))

print(answer if answer!=sys.maxsize else -1)