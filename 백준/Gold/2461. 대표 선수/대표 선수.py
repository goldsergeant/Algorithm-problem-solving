import sys
from heapq import heappush, heappop
from bisect import bisect_left

N, M = map(int, sys.stdin.readline().split())
classes = [sorted(map(int, sys.stdin.readline().split())) for _ in range(N)]
# classes.sort(key=lambda x:x[0])
answer = sys.maxsize
if N == 1:
    print(0)
    exit()

heap=[]
max_num=0
for i in range(N):
    heappush(heap,(classes[i][0],i,0))
    max_num = max(max_num, classes[i][0])

while heap:
    num,i,j = heappop(heap)
    answer=min(answer,abs(max_num-num))

    if j+1==M:
        break

    heappush(heap,(classes[i][j+1],i,j+1))
    max_num=max(max_num, classes[i][j+1])

print(answer)