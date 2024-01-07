import sys
from heapq import *

T=int(sys.stdin.readline())
for _ in range(T):
    N=int(sys.stdin.readline())
    files=list(map(int,sys.stdin.readline().split()))
    heapify(files)
    answer=0
    while len(files)>1:
        a,b=heappop(files),heappop(files)
        answer+=a+b
        heappush(files,a+b)

    print(answer)