import sys
from heapq import heappush,heappop

N=int(sys.stdin.readline())
min_q=[]
max_q=[]
for i in range(N):
    num=int(sys.stdin.readline())
    if i%2==0:
        heappush(max_q,-num)
    else:
        heappush(min_q,num)

    if not min_q:
        print(-max_q[0])
        continue

    if min_q[0]< -max_q[0]:
        a,b=heappop(min_q),-heappop(max_q),
        heappush(min_q,b)
        heappush(max_q,-a)


    print(-max_q[0])