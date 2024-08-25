import sys
from heapq import heappop,heappush

N,K=map(int,sys.stdin.readline().split())
customers=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
heap=[]
outs=[]
for i in range(1,K+1):
    heappush(heap,(0,i))

for id,minutes in customers:
    time,counter_num=heappop(heap)
    heappush(heap,(time+minutes,counter_num))
    outs.append((time+minutes,counter_num,id))

outs.sort(key=lambda x:(x[0],-x[1]))
answer=0

idx=1
for time,counter_num,id in outs:
    answer+=id*idx
    idx+=1

print(answer)