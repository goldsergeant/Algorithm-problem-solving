import collections
import sys

N,W,L=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))

queue=collections.deque()
total_weight=0
time=0
for weight in arr:
    while True:
        if len(queue)==W:
            total_weight-=queue.popleft()
        if total_weight+weight<=L:
            break
        queue.append(0)
        time+=1
    queue.append(weight)
    total_weight+=weight
    time+=1

print(time+W)