import collections
import sys

N, M = map(int, sys.stdin.readline().split())
boards = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
score_board=[[0 for _ in range(M)] for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
answer=0

def bfs(s_r,s_c,visited):
    zero_points=set()
    total=0
    q=collections.deque([(s_r,s_c)])
    visited[s_r][s_c]=True

    while q:
        r,c=q.popleft()
        total+=1

        for dy,dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            n_r=r+dy
            n_c=c+dx
            if 0<=n_r<N and 0<=n_c<M:
                if boards[n_r][n_c]==1 and not visited[n_r][n_c]:
                    visited[n_r][n_c]=True
                    q.append((n_r,n_c))
                elif boards[n_r][n_c]==0:
                    zero_points.add((n_r,n_c))

    for r,c in zero_points:
        score_board[r][c]+=total

for i in range(N):
    for j in range(M):
        if boards[i][j]==1 and not visited[i][j]:
            bfs(i,j,visited)

for i in range(N):
    for j in range(M):
        if boards[i][j]==0:
            answer=max(answer,score_board[i][j]+1)

print(answer)