import collections
import sys

def bfs(s_r,s_c):
    q=collections.deque([(s_r,s_c,0,0)])
    dust_num=0
    field_to_dust_num=dict()

    for i in range(H):
        for j in range(W):
            if board[i][j]=="*":
                field_to_dust_num[(i,j)]=dust_num
                dust_num+=1

    visited=[[[False for _ in range(1<<dust_num)] for _ in range(W)] for _ in range(H)]
    all_bit=0
    for i in range(dust_num):
        all_bit=all_bit|(1<<i)

    while q:
        r,c,dust_bit,move_cnt=q.popleft()
        if dust_bit==all_bit:
            return move_cnt

        for dr,dc in (1,0),(0,1),(-1,0),(0,-1):
            nr,nc=r+dr,c+dc
            if 0<=nr<H and 0<=nc<W and board[nr][nc]!="x":
                if board[nr][nc]=='*':
                    next_bit=dust_bit|(1<<field_to_dust_num[(nr,nc)])
                    if not visited[nr][nc][next_bit]:
                        visited[nr][nc][next_bit]=True
                        q.append((nr,nc,next_bit,move_cnt+1))
                else:
                    if not visited[nr][nc][dust_bit]:
                        visited[nr][nc][dust_bit]=True
                        q.append((nr,nc,dust_bit,move_cnt+1))

    return -1
while True:
    W,H=map(int,sys.stdin.readline().split())
    if W==0 and H==0:break

    board=[list(sys.stdin.readline().strip()) for _ in range(H)]
    answer=0
    for i in range(H):
        for j in range(W):
            if board[i][j]=="o":
                answer=bfs(i,j)

    print(answer)