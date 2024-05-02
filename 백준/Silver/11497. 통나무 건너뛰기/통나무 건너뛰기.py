import collections
import sys
from heapq import heappop,heappush,heapify

T=int(sys.stdin.readline())
for _ in range(T):
    N=int(sys.stdin.readline())
    heap=list(map(lambda x:(-int(x),int(x)),sys.stdin.readline().split()))
    heapify(heap)
    deq=collections.deque()
    answer=0

    direct=False
    while heap:
        num=heappop(heap)[1]
        if not direct:
            deq.appendleft(num)
        else:
            deq.append(num)
        direct=not direct

    arr=list(deq)
    for i in range(1,len(arr)):
        answer=max(answer,abs(arr[i]-arr[i-1]))
    print(answer)