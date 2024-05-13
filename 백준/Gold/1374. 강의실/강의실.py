import sys
from heapq import heappop,heappush,heappushpop

N=int(sys.stdin.readline())
answer=1
lectures=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
lectures.sort(key=lambda x:(x[1],x[2]))

heap=[]
for num,start,end in lectures:
    if not heap:
        heappush(heap,end)
        continue

    while heap and heap[0]<=start:
        heappop(heap)

    heappush(heap,end)
    answer=max(answer,len(heap))

print(answer)