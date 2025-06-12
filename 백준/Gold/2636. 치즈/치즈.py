import collections
import sys

H,W=map(int,sys.stdin.readline().split())
board=[list(map(int,sys.stdin.readline().split())) for _ in range(H)]
last_cheese_cnt=0

q1=collections.deque([(0,0)])
q2=collections.deque()
visited=[[False for _ in range(W)] for _ in range(H)]
visited[0][0]=True
time=0
while True:
    while q1:
        r,c=q1.popleft()
        board[r][c]=0
        for dr,dc in ((0,1),(0,-1),(1,0),(-1,0)):
            nr,nc=r+dr,c+dc
            if 0<=nr<H and 0<=nc<W:
                if visited[nr][nc]:
                    continue

                visited[nr][nc]=True
                if board[nr][nc]==0:
                    q1.append((nr,nc))
                else:
                    q2.append((nr,nc))

    if not q2:
        print(time)
        print(last_cheese_cnt)
        break
    last_cheese_cnt=len(q2)
    q1=q2
    q2=collections.deque()
    time+=1
