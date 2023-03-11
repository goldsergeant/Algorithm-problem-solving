import collections
import sys

n,m=map(int,sys.stdin.readline().split())
miro=[]
dy=[0,0,1,-1]
dx=[1,-1,0,0]
visited=[[[False]*2 for i in range(m)] for i in range(n)]

for i in range(n):
    miro.append(list(sys.stdin.readline().strip()))

queue=collections.deque()
queue.append((0,0,1,1))    #순서대로 y,x,count,chance
visited[0][0][0]=True
while queue:
    y,x,count,chance=queue.popleft()
    if y==n-1 and x==m-1:
        print(count)
        exit()
    for i in range(4):
        ny=y+dy[i]
        nx=x+dx[i]
        if ny<0 or ny>n-1 or nx<0 or nx>m-1:
            continue

        if not visited[ny][nx][chance] and miro[ny][nx]=='0':
            queue.append((ny,nx,count+1,chance))
            visited[ny][nx][chance]=True

        if miro[ny][nx]=='1' and chance==1:
            queue.append((ny,nx,count+1,0))
            visited[ny][nx][0] = True
print(-1)