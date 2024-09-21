import collections
import sys

def bfs(s_r,s_c):
    q=collections.deque([(s_r,s_c)])
    points=[]
    chunk_points=set()
    visited[s_r][s_c]=True
    while q:
        r,c=q.popleft()
        points.append((r,c))

        for dy,dx in [(-1,0),(1,0),(0,-1),(0,1)]:
            ny,nx=r+dy,c+dx
            if ny<0 or nx<0 or ny>N-1 or nx>M-1:
                continue
            if not visited[ny][nx] and board[ny][nx]==0:
                visited[ny][nx]=True
                q.append((ny,nx))

    for y,x in points:
        for dy,dx in [(-1,0),(1,0),(0,-1),(0,1)]:
            ny,nx=y+dy,x+dx
            if ny<0 or nx<0 or ny>N-1 or nx>M-1:
                continue

            if board[ny][nx]==1:
                chunk_points.add((ny,nx))

    for y,x in chunk_points:
        answer[y][x]+=len(points)

N,M=map(int,sys.stdin.readline().split())
board=[list(map(int,list(sys.stdin.readline().rstrip()))) for _ in range(N)]
answer=[[0 for _ in range(M)] for _ in range(N)]
visited=[[False for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        if board[i][j]==0 and not visited[i][j]:
            bfs(i,j)

for i in range(N):
    for j in range(M):
        if board[i][j]==1:
            answer[i][j]+=1
# for arr in chunk:
#     print(*arr)
for arr in answer:
    print(*map(lambda x:x%10 if x>0 else 0,arr),sep='')
