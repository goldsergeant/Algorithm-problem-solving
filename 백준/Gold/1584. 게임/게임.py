import collections
import sys

warn_points=[]
death_points=[]
visited=[[False for _ in range(501)] for _ in range(501)]
dy=[-1,1,0,0]
dx=[0,0,-1,1]

def is_in_area(x,y,point_arr):
    for point in point_arr:
        x1, y1, x2, y2 = point
        if (x1 <= x <= x2 or x2<=x<=x1) and (y1 <= y <= y2 or y2<=y<=y1):
            return True

    return False

n=int(sys.stdin.readline())
for _ in range(n):
    warn_points.append(list(map(int, sys.stdin.readline().split())))
m=int(sys.stdin.readline())
for _ in range(m):
    death_points.append(list(map(int, sys.stdin.readline().split())))
q=collections.deque([(0,0,0)])

while q:
    y,x,losed_cnt=q.popleft()
    if y==500 and x==500:
        print(losed_cnt)
        exit()

    for i in range(4):
        n_y,n_x=y+dy[i],x+dx[i]
        if n_y<0 or n_x<0 or n_y>500 or n_x>500:
            continue

        if is_in_area(n_x,n_y,death_points):
            continue

        if is_in_area(n_x,n_y,warn_points) and not visited[n_y][n_x]:
            visited[n_y][n_x]=True
            q.append((n_y,n_x,losed_cnt+1))
        elif not visited[n_y][n_x]:
            visited[n_y][n_x]=True
            q.appendleft((n_y,n_x,losed_cnt))

print(-1)