import collections
import sys

a,b,n,m=map(int,sys.stdin.readline().split())
visited=[sys.maxsize for _ in range(100001)]
dx=[1,-1]
jump_x=[a,b,-a,-b]
mul_x=[a,b]
queue=collections.deque()
queue.appendleft((n,0))
visited[n]=True
while queue:
    pos,depth=queue.pop()
    for i in range(2):
        n_x=pos+dx[i]
        if n_x<0 or n_x>100000:
            continue
        if depth+1<visited[n_x]:
            visited[n_x]=depth+1
            queue.appendleft((n_x,depth+1))

    for i in range(4):
        n_x = pos + jump_x[i]
        if n_x < 0 or n_x > 100000:
            continue
        if depth+1 < visited[n_x]:
            visited[n_x] = depth+1
            queue.appendleft((n_x, depth + 1))

    for i in range(2):
        n_x=pos*mul_x[i]
        if n_x<0 or n_x>100000:
            continue
        if depth+1 < visited[n_x]:
            visited[n_x] = depth+1
            queue.appendleft((n_x, depth + 1))

print(visited[m])