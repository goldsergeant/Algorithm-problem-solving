import sys
from heapq import heappush,heappop
def dijkstra():
    heap=[]
    total_water=0
    visited=[[False for _ in range(M)] for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if i == 0 or i == N - 1 or j == 0 or j == M - 1:
                heappush(heap, (board[i][j], i, j))
                visited[i][j] = True

    while heap:
        height,r,c=heappop(heap)

        for dr,dc in [(1,0),(0,1),(-1,0),(0,-1)]:
            nr,nc=r+dr,c+dc
            if 0<=nr<N and 0<=nc<M:
                if not visited[nr][nc] and not visited[nr][nc]:
                    if board[nr][nc]<height:
                        total_water+=height-board[nr][nc]
                    visited[nr][nc]=True
                    heappush(heap,(max(height,board[nr][nc]),nr,nc))

    return total_water
N,M=map(int,sys.stdin.readline().split())
board=[list(map(int,sys.stdin.readline().strip())) for _ in range(N)]

print(dijkstra())