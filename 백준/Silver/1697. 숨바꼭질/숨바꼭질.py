import collections
import sys

n,k=map(int,sys.stdin.readline().split())
queue=collections.deque([(n,0)])
visited=[False for i in range(100001)]
visited[n]=True
while queue:
    point,second=queue.popleft()
    if point==k:
        print(second)
        exit()
    if point-1>=0 and not visited[point-1]:
        queue.append((point-1,second+1))
        visited[point-1]=True
    if point+1<=100000 and not visited[point+1]:
        queue.append((point+1,second+1))
        visited[point + 1] = True
    if 2*point<=100000 and not visited[point*2]:
        queue.append((point*2,second+1))
        visited[point*2]=True
