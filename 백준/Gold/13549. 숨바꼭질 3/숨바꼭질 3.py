import collections
import sys

n,k=map(int,sys.stdin.readline().split())
queue=collections.deque()
queue.append((n,0))
visited=[False for i in range(100000+1)]
visited[n]=True
while queue:
    position,second=queue.popleft()
    if position==k:
        print(second)
        break

    if position * 2 <= 100000 and not visited[position * 2]:
        queue.append((position * 2, second))
        visited[position * 2] = True
    if position>0 and not visited[position-1]:
        queue.append((position-1,second+1))
        visited[position-1]=True
    if position+1<=k and not visited[position+1]:
        queue.append((position+1,second+1))
        visited[position+1]=True
