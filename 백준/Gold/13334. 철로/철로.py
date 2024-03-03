import sys
from heapq import heappush,heappop

N = int(sys.stdin.readline())
pairs = [tuple(sorted(map(int, sys.stdin.readline().split()))) for _ in range(N)]
D = int(sys.stdin.readline())
answer = 0
pairs.sort(key=lambda x: (x[1], x[0]))
heap=[]

for h,o in pairs:
    if o-h<=D:
        heappush(heap,h)

    while heap and heap[0]+D<o:
        heappop(heap)

    answer=max(answer,len(heap))

print(answer)
