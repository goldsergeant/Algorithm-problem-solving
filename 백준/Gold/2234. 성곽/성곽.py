import collections
import sys

dir = [(-1,0),(1,0),(0,-1),(0,1)]

def get_impossible_dir(i,j):
    impossible_dir=set()
    tmp=board[i][j]

    if tmp>=8:
        impossible_dir.add((1,0))
        tmp-=8
    if tmp>=4:
        impossible_dir.add((0,1))
        tmp-=4
    if tmp>=2:
        impossible_dir.add((-1,0))
        tmp-=2
    if tmp>=1:
        impossible_dir.add((0,-1))

    return impossible_dir

def bfs(i,j,num):
    q=collections.deque([(i,j)])
    visited[i][j]=True
    count=0
    while q:
        r,c=q.popleft()
        room_num[r][c]=num
        count+=1
        impossible_dir=get_impossible_dir(r,c)
        for dy,dx in dir:
            ny,nx=r+dy,c+dx
            if 0<=ny<N and 0<=nx<M:
                if not visited[ny][nx] and (dy,dx) not in impossible_dir:
                    visited[ny][nx]=True
                    q.append((ny,nx))

    return count

M,N=map(int,sys.stdin.readline().split())
board=[[*map(int,sys.stdin.readline().split())] for _ in range(N)]
room_num=[[0 for _ in range(M)] for _ in range(N)]
room_cnt=0
most_wide=0
remove_most_wide=0
room_area=dict()
visited=[[False for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            room_cnt+=1
            area=bfs(i,j,room_cnt)
            most_wide=max(most_wide,area)
            room_area[room_cnt]=area

print(room_cnt)
print(most_wide)

for i in range(N):
    for j in range(M):
        for dy,dx in dir:
            ny,nx=i+dy,j+dx
            if 0<=ny<N and 0<=nx<M:
                if room_num[i][j]!=room_num[ny][nx]:
                    a,b=room_num[i][j],room_num[ny][nx]
                    remove_most_wide=max(remove_most_wide,room_area[a]+room_area[b])

print(remove_most_wide)
