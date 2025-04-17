import collections
import sys
from heapq import heappop, heappush, heapify

C, N = map(int, sys.stdin.readline().split())
chicken_times = list(int(sys.stdin.readline()) for _ in range(C))
cow_times = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
chicken_times.sort()
cow_times.sort(key=lambda x:(x[1],x[0]))
vis=[False for _ in range(len(chicken_times))]
answer=0
for s,e in cow_times:
    for i,t in enumerate(chicken_times):
        if s<=t<=e and not vis[i]:
            vis[i]=True
            answer+=1
            break
print(answer)