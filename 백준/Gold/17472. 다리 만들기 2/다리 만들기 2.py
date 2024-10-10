import collections
import sys

def dfs(r, c, num):
    board[r][c]=num
    points_of_island[num].append((r,c))
    number_visited[r][c]=True
    for dy,dx in (-1,0),(1,0),(0,-1),(0,1):
        ny,nx=r+dy,c+dx
        if ny<0 or nx<0 or ny >= N or nx >= M:
            continue
        if board[ny][nx]!=0 and not number_visited[ny][nx]:
            dfs(ny, nx, num)

def get_outlines_of_island(island_num):
    outlines=[]
    for y,x in points_of_island[island_num]:
        for dy,dx in (-1,0),(1,0),(0,-1),(0,1):
            ny,nx=y+dy,x+dx
            if ny<0 or nx<0 or ny >= N or nx >= M:
                continue
            if board[ny][nx]==0:
                outlines.append((y,x))
                break
    return outlines

def build_bridge_of_island(island_num):
    outlines=get_outlines_of_island(island_num)
    for y,x in outlines:
        for dy,dx in (-1,0),(1,0),(0,-1),(0,1):
            ny,nx=y+dy,x+dx
            bridge_length = 1
            while 0<=ny<N and 0<=nx<M and board[ny][nx]==0:
                ny,nx=ny+dy,nx+dx
                bridge_length+=1
            bridge_length-=1
            if 0<=ny<N and 0<=nx<M and board[ny][nx]!=island_num and bridge_length>=2:
                bridges.add((bridge_length,min(island_num,board[ny][nx]),max(island_num,board[ny][nx])))

def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

def union(a,b):
    a=find(a)
    b=find(b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b


N,M=map(int,sys.stdin.readline().split())
board=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
bridges=set()
number_visited=[[False for _ in range(M)] for _ in range(N)]
points_of_island = collections.defaultdict(list)
parent=[0]
answer=0

num=0
for i in range(N):
    for j in range(M):
        if board[i][j]!=0 and not number_visited[i][j]:
            num+=1
            parent.append(num)
            dfs(i, j, num)

for key in points_of_island.keys():
    build_bridge_of_island(key)

for cost,a,b in sorted(bridges):
    if find(a)!=find(b):
        union(a,b)
        answer+=cost

# for arr in board:
#     print(arr)
# print(sorted(bridges))
tmp=set()
for i in range(1,num+1):
    tmp.add(find(i))

print(answer if len(tmp)==1 else -1)
