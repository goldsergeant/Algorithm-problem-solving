import collections
import sys
dx=[0,0,0,0,1,-1]
dy=[0,0,1,-1,0,0]
dz=[1,-1,0,0,0,0]

queue=collections.deque()
m,n,h=map(int,sys.stdin.readline().split())
tomatos=[[] for _ in range(h)]
for i in range(h):
    for _ in range(n):
        tomatos[i].append(list(map(int,sys.stdin.readline().split())))


for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomatos[i][j][k]==1:
                queue.append((i,j,k,tomatos[i][j][k]))

while queue:
    z,y,x,day=queue.popleft()
    for i in range(6):
        nz=z+dz[i]
        ny=y+dy[i]
        nx=x+dx[i]
        if nz<0 or nz>h-1 or ny<0 or ny>n-1 or nx<0 or nx>m-1:
            continue
        if tomatos[nz][ny][nx]==0:
            queue.append((nz,ny,nx,day+1))
            tomatos[nz][ny][nx]=day+1

max_day=-sys.maxsize
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomatos[i][j][k]==0:
                print(-1)
                exit()
            max_day=max(max_day,tomatos[i][j][k])
print(max_day-1)