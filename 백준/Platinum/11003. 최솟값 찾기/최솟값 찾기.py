import collections
import heapq
import sys

n,l=map(int,sys.stdin.readline().split())
a=list(map(int,sys.stdin.readline().split()))
answer=[]
q=collections.deque()
for i in range(n):
    if q and q[0][1]==i-l:
        q.popleft()

    while q and a[i]<q[-1][0]:
        q.pop()
    q.append((a[i],i))
    answer.append(q[0][0])

print(' '.join(map(str,answer)))