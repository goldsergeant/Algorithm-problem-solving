import collections
import sys

def get_fire_score():
    fire_score_board=[[sys.maxsize for _ in range(W)] for _ in range(H)]
    q=collections.deque()

    for i in range(H):
        for j in range(W):
            if board[i][j]=='*':
                q.append((i,j,0))
                fire_score_board[i][j]=0
    while q:
        r,c,t=q.popleft()

        for dr,dc in (-1,0),(1,0),(0,-1),(0,1):
            nr,nc=r+dr,c+dc
            if 0<=nr<H and 0<=nc<W:
                if board[nr][nc]!='#' and t+1<fire_score_board[nr][nc]:
                    fire_score_board[nr][nc]=t+1
                    q.append((nr,nc,t+1))

    return fire_score_board

def bfs(s_r,s_c):
    visited=[[False for _ in range(W)] for _ in range(H)]
    visited[s_r][s_c]=True
    q=collections.deque([(s_r,s_c,0)])
    while q:
        r,c,t=q.popleft()

        for dr,dc in (-1,0),(1,0),(0,-1),(0,1):
            nr,nc=r+dr,c+dc
            if nr<0 or nc<0 or nr>=H or nc>=W:
                return t+1
            if board[nr][nc]!='#' and t+1<fire_score_board[nr][nc] and not visited[nr][nc]:
                visited[nr][nc]=True
                q.append((nr,nc,t+1))

    return 'IMPOSSIBLE'

T=int(sys.stdin.readline())
for _ in range(T):
    W,H=map(int,sys.stdin.readline().split())
    board=[sys.stdin.readline().strip() for _ in range(H)]
    fire_score_board=get_fire_score()

    s_r,s_c=0,0
    for i in range(H):
        for j in range(W):
            if board[i][j]=='@':
                s_r,s_c=i,j

    print(bfs(s_r,s_c))