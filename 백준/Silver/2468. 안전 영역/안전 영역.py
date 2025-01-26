import sys
sys.setrecursionlimit(100000)

def dfs(i,j):
    visited[i][j]=True
    for di,dj in (-1,0),(1,0),(0,-1),(0,1),:
        ni, nj = i+di,j+dj
        if 0<=ni<N and 0<=nj<N and not visited[ni][nj] and not is_flooded[ni][nj]:
            dfs(ni,nj)



N=int(sys.stdin.readline())
board=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
max_height=max(max(board[i]) for i in range(N))
answer=0
for rain_height in range(0,max_height):
    is_flooded=[[False for _ in range(N)] for _ in range(N)]
    visited=[[False for _ in range(N)] for _ in range(N)]
    sector=0
    for i in range(N):
        for j in range(N):
            if board[i][j]<=rain_height:
                is_flooded[i][j]=True

    for i in range(N):
        for j in range(N):
            if not is_flooded[i][j] and not visited[i][j]:
                sector+=1
                dfs(i,j)

    answer=max(answer,sector)

print(answer)
