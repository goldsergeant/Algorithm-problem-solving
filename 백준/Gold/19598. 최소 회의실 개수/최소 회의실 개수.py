import sys
from heapq import heappop,heappush

N=int(sys.stdin.readline())
times=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
times.sort(key=lambda x:(x[0],x[1]))
answer=0
heap=[]
for i in range(N):
    cur_s,cur_e=times[i]
    if not heap:
        heappush(heap,cur_e)
        answer+=1
    else:
        if heap[0]<=cur_s:
            heappop(heap)
            heappush(heap,cur_e)
        else:
            heappush(heap,cur_e)
            answer+=1
print(answer)