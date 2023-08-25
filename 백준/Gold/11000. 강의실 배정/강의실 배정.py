import collections
import heapq
import sys

n=int(input())
time=[]
dp=[0]*(n+1)
q=[]
for i in range(1,n+1):
    a,b=map(int,sys.stdin.readline().split())
    time.append((a,b))

time.sort()
q.append(time[0][1])

for i in range(1,n):
    end_time=heapq.heappop(q)
    if end_time>time[i][0]:
        heapq.heappush(q,end_time)
        heapq.heappush(q,time[i][1])
    else:
        heapq.heappush(q,time[i][1])

print(len(q))
