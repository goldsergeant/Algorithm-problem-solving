import collections
import sys

T=int(sys.stdin.readline())

def bfs():
    visited=[False for _ in range(len(points))]
    visited[0]=True
    q = collections.deque()
    q.append(points[0])
    while q:
        x, y = q.popleft()
        if x == points[-1][0] and y == points[-1][1]:
            return True
        for i,p in enumerate(points):
            nx,ny=p
            if abs(nx-x) +abs(ny-y)<=1000 and not visited[i]:
                visited[i]=True
                q.append((nx,ny))

    return False

for _ in range(T):
    n=int(sys.stdin.readline())
    points=list(tuple(map(int,sys.stdin.readline().split())) for _ in range(n+2))

    print('happy' if bfs() else 'sad')
