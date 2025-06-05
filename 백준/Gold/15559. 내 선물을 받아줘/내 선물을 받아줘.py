import collections
import sys

N,M=map(int,sys.stdin.readline().split())
board=[list(sys.stdin.readline().rstrip()) for _ in range(N)]
zone=[[0 for _ in range(M)] for _ in range(N)]
zone_cnt=0

def bfs(s_r,s_c):
    global zone_cnt
    q=collections.deque([(s_r,s_c)])
    zone_cnt += 1
    zone[s_r][s_c]=zone_cnt
    points=[]
    while q:
        r,c=q.popleft()
        points.append((r,c))
        nr,nc=r,c
        if board[r][c]=='N':
            nr-=1
        elif board[r][c]=='S':
            nr+=1
        elif board[r][c]=='W':
            nc-=1
        elif board[r][c]=='E':
            nc+=1

        if not zone[nr][nc]:
            zone[nr][nc]=zone_cnt
            q.append((nr,nc))
        else:
            if zone[nr][nc]!=zone_cnt:
                zone_cnt-=1
                for r,c in points:
                    zone[r][c]=zone[nr][nc]


for i in range(N):
    for j in range(M):
        if not zone[i][j]:
            bfs(i,j)
print(zone_cnt)