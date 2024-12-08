import sys
from heapq import heappush,heappop

N=int(sys.stdin.readline())
lines=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
lines.sort(key=lambda x:(x[0],x[1]))
heap=[]
answer=0

for a,b in lines:
    while heap and heap[0]<=a:
        heappop(heap)

    heappush(heap,b)
    answer=max(answer,len(heap))

print(answer)