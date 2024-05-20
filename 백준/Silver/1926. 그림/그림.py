import sys
sys.setrecursionlimit(1000000)

def dfs(r,c):
    global total
    total+=1
    board[r][c]=0

    for dr,dc in (0,-1),(0,1),(-1,0),(1,0),:
        nr,nc=r+dr,c+dc
        if 0<=nr<N and 0<=nc<M:
            if board[nr][nc]==1:
                dfs(nr,nc)

N,M=map(int,sys.stdin.readline().split())
board=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
answer=0
cnt=0
for i in range(N):
    for j in range(M):
        if board[i][j]==1:
            total=0
            dfs(i,j)
            answer=max(answer,total)
            cnt+=1

print(cnt)
print(answer)
