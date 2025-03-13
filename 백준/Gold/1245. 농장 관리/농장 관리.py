import collections
import sys

def bfs(s_r,s_c):
    q=collections.deque([(s_r,s_c)])
    visited[s_r][s_c]=True
    border_points=[]
    while q:
        r,c=q.popleft()
        for dr,dc in (1,0),(-1,0),(0,-1),(0,1),(1,1),(1,-1),(-1,1),(-1,-1):
            nr,nc=r+dr,c+dc
            if 0<=nr<N and 0<=nc<M:
                if board[nr][nc]==board[r][c] and not visited[nr][nc]:
                    visited[nr][nc]=True
                    q.append((nr,nc))
                elif board[nr][nc]!=board[r][c]:
                    border_points.append(board[nr][nc])

    if all(x<board[s_r][s_c] for x in border_points):
        return True
    return False

N,M=map(int,sys.stdin.readline().split())
board=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
visited=[[False for _ in range(M)] for _ in range(N)]
answer=0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            if bfs(i,j):
                answer+=1
print(answer)