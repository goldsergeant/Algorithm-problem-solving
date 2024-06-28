import collections
import sys

dir = [
    [(-1, 0), (-2, -1), (-3, -2)],
    [(-1, 0), (-2, 1), (-3, 2)],
    [(1, 0), (2, -1), (3, -2)],
    [(1, 0), (2, 1), (3, 2)],
    [(0, -1), (-1, -2), (-2, -3)],
    [(0, -1), (1, -2), (2, -3)],
    [(0, 1), (-1, 2), (-2, 3)],
    [(0, 1), (1, 2), (2, 3)],
]

unit_position = [*map(int, sys.stdin.readline().split())]
target_position = [*map(int, sys.stdin.readline().split())]
visited=[[False for _ in range(9)] for _ in range(10)]
q=collections.deque([(unit_position[0],unit_position[1],0)])
visited[unit_position[0]][unit_position[1]]=True

while q:
    y,x,cnt=q.popleft()
    if [y,x]==target_position:
        print(cnt)
        break

    for pos in dir:
        flag=True
        for dy,dx in pos:
            ny,nx=dy+y,dx+x
            if ny<0 or nx<0 or ny>=10 or nx>=9:
                flag=False
                break
            if [ny,nx]==target_position and (dy,dx)!=pos[-1]:
                flag=False
                break

        if not flag:
            continue

        ny,nx=y+pos[-1][0],x+pos[-1][1]
        if not visited[ny][nx]:
            visited[ny][nx]=True
            q.append((ny,nx,cnt+1))

