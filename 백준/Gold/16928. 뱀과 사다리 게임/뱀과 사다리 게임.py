import collections
import sys

n, m = map(int,sys.stdin.readline().split())
leathers = dict()
snake=dict()
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    leathers[x] = y
for _ in range(m):
    x,y=map(int,sys.stdin.readline().split())
    snake[x]=y

queue = collections.deque()
queue.append((1, 0))
visited=[False for i in range(101)]
while queue:
    point, count = queue.popleft()
    if point == 100:
        print(count)
        break
    for i in range(1, 7):
        next_point = point + i
        if next_point>100 or visited[next_point]:
            continue
        if leathers.get(next_point):
            next_point=leathers[next_point]
        if snake.get(next_point):
            next_point=snake[next_point]
        if not visited[next_point]:
            queue.append((next_point,count+1))
            visited[next_point]=True