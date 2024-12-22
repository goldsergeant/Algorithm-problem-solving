import collections
import sys
from heapq import heappush, heappop, heapify
N=int(sys.stdin.readline())
times=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
times.sort(key=lambda x:x[0])
seat_cnt=collections.defaultdict(int)
heap=[]
seat_num_heap=[i for i in range(1,N+1)]
heapify(seat_num_heap)

for start,end in times:
        while heap and heap[0][0]<start:
            heappush(seat_num_heap,heappop(heap)[1])

        seat_num=heappop(seat_num_heap)
        seat_cnt[seat_num]+=1
        heappush(heap,(end,seat_num))

print(len(seat_cnt.keys()))
for key in sorted(seat_cnt.keys()):
    print(seat_cnt[key],end=' ')