import sys
from collections import deque

key={'a':1,'b':1<<1,'c':1<<2,'d':1<<3,'e':1<<4,'f':1<<5}

def bfs(s_r,s_c):
    q=deque([(s_r,s_c,0,0)])
    visited=[[[False for _ in range(1<<6)] for _ in range(M)] for _ in range(N)]
    visited[s_r][s_c][0]=True

    while q:
        r,c,distance,has_key=q.popleft()
        if board[r][c]=='1':
            return distance

        for dr,dc in (-1,0),(1,0),(0,-1),(0,1):
            nr,nc=r+dr,c+dc
            if 0<=nr<N and 0<=nc<M:
                if board[nr][nc]=='.' or board[nr][nc].isdigit():
                    if not visited[nr][nc][has_key]:
                        visited[nr][nc][has_key]=True
                        q.append((nr,nc,distance+1,has_key))

                elif board[nr][nc].islower():
                    next_has_key=has_key|key[board[nr][nc]]
                    if not visited[nr][nc][next_has_key]:
                        visited[nr][nc][next_has_key]=True
                        q.append((nr,nc,distance+1,next_has_key))

                elif board[nr][nc].isupper():
                    if not visited[nr][nc][has_key] and has_key&key[board[nr][nc].lower()]:
                        visited[nr][nc][has_key]=True
                        q.append((nr,nc,distance+1,has_key))
    return -1

N,M=map(int,sys.stdin.readline().split())
board=[list(sys.stdin.readline().rstrip()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if board[i][j]=='0':
            print(bfs(i,j))
            break