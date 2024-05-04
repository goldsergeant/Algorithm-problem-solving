import collections
import sys
from heapq import heappush,heappop

T=int(sys.stdin.readline())
for _ in range(T):
    K=int(sys.stdin.readline())
    max_heap=[]
    min_heap=[]
    counter=collections.Counter()
    for _ in range(K):
        Q,N=sys.stdin.readline().split()
        N=int(N)
        if Q=='I':
            heappush(max_heap,-N)
            heappush(min_heap,N)
            counter[N]+=1
        elif Q=='D':
            if N==1:
                if max_heap:
                    num=-heappop(max_heap)
                    counter[num]-=1
            elif N==-1:
                if min_heap:
                    num=heappop(min_heap)
                    counter[num]-=1
            while max_heap and counter[-max_heap[0]]==0:
                heappop(max_heap)
            while min_heap and counter[min_heap[0]]==0:
                heappop(min_heap)

    if max_heap:
        print(-max_heap[0],min_heap[0])
    else:
        print('EMPTY')