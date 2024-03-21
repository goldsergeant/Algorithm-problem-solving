import sys
sys.setrecursionlimit(10000000)

N,M=map(int,sys.stdin.readline().split())
board=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
visited=[[False for _ in range(M)] for _ in range(N)]
answer=0

def dfs(r,c):
    visited[r][c]=True
    for dr,dc in ((1,0),(0,1),(-1,0),(0,-1),):
        nr,nc=r+dr,c+dc
        if nr<0:
            nr=N-1
        elif nr>N-1:
            nr=0

        if nc<0:
            nc=M-1
        elif nc>M-1:
            nc=0

        if not visited[nr][nc] and board[nr][nc]==0:
            dfs(nr,nc)

for i in range(N):
    for j in range(M):
        if board[i][j]==0 and not visited[i][j]:
            answer+=1
            dfs(i,j)
print(answer)