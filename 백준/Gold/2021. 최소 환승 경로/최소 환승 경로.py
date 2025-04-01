import collections
import sys
from heapq import heappush, heappop

N,L=map(int,sys.stdin.readline().split())
hoseon=[set() for _ in range(N+1)]
route=[[] for _ in range(L)]
for h in range(L):
    arr= list(map(int,sys.stdin.readline().split()))
    hoseon[arr[0]].add(h)
    route[h].append(arr[0])
    for i in range(1,len(arr)-1):
        hoseon[arr[i]].add(h)
        hoseon[arr[i-1]].add(h)
        route[h].append(arr[i])
S,E=map(int,sys.stdin.readline().split())
visited=[False for _ in range(N+1)]
q = []
answer=sys.maxsize
for h in hoseon[S]:
    heappush(q,(0,h))
    visited[h]=True

while q:
    transfer_cnt,cur_hoseon=heappop(q)
    for node in route[cur_hoseon]:
        if node==E:
            print(transfer_cnt)
            exit()
        else:
            next_hoseon=hoseon[node]
            for h in next_hoseon:
                if not visited[h]:
                    visited[h]=True
                    heappush(q,(transfer_cnt+1,h))



print(answer if answer<sys.maxsize else -1)