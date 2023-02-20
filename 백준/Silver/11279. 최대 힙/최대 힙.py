import heapq
import sys

n=int(sys.stdin.readline())
heap=[]
for _ in range(n):
    x=int(sys.stdin.readline())
    if x==0:
        print(heapq.heappop(heap)[1] if len(heap)>0 else 0)
    else:
        heapq.heappush(heap,(-x,x))
