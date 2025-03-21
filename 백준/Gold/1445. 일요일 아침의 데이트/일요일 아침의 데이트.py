import sys
from heapq import heappush,heappop
N,M=map(int,sys.stdin.readline().split())
board=[list(sys.stdin.readline().strip()) for _ in range(N)]
heap=[]
visited=[[(sys.maxsize,sys.maxsize) for _ in range(M)] for _ in range(N)]
e_r,e_c=0,0
for i in range(N):
    for j in range(M):
        if board[i][j]=='S':
            heap=[(0,0,i,j)]
            visited[i][j]=(0,0)
        elif board[i][j]=='F':
            e_r,e_c=i,j

while heap:
    garbage,adj_garbage,r,c=heappop(heap)
    if (r,c)==(e_r,e_c):
        print(garbage,adj_garbage)
        break

    for dr,dc in (0,-1),(0,1),(-1,0),(1,0),:
        nr,nc=r+dr,c+dc
        if 0<=nr<N and 0<=nc<M:
            n_garbage,n_adj_garbage=garbage,adj_garbage
            if board[nr][nc]=='g':
                n_garbage+=1
            else:
                is_adj_garbage=False
                for dr2,dc2 in (0,-1),(0,1),(-1,0),(1,0),:
                    if board[nr][nc]=='F':
                        break
                    nr2,nc2=nr+dr2,nc+dc2
                    if 0<=nr2<N and 0<=nc2<M:
                        if board[nr2][nc2]=='g':
                            is_adj_garbage=True
                            break
                if is_adj_garbage:
                    n_adj_garbage+=1

            if n_garbage<visited[nr][nc][0] or (n_garbage==visited[nr][nc][0] and n_adj_garbage<visited[nr][nc][1]):
                visited[nr][nc]=(n_garbage,n_adj_garbage)
                heappush(heap,(n_garbage,n_adj_garbage,nr,nc))
