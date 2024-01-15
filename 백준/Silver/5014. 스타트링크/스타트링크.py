import collections
import sys

F,S,G,U,D=map(int,sys.stdin.readline().split())

def bfs(start):
    visited = [False for i in range(F + 1)]
    visited[start]=True
    q=collections.deque([(S,0)])
    while q:
        floor,cnt=q.popleft()
        if floor==G:
            return cnt

        if floor+U<=F and not visited[floor+U]:
            visited[floor+U]=True
            q.append((floor+U,cnt+1))

        if floor-D>=1 and not visited[floor-D]:
            visited[floor-D]=True
            q.append((floor-D,cnt+1))

    return 'use the stairs'
print(bfs(S))
