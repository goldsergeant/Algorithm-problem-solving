import collections
import sys
from heapq import heappop,heappush

N=int(sys.stdin.readline())
T,M=map(int,sys.stdin.readline().split())
L=int(sys.stdin.readline())
graph=collections.defaultdict(list)
answer=sys.maxsize
for _ in range(L):
    a,b,t,c=map(int,sys.stdin.readline().split())
    graph[a].append((b,t,c))
    graph[b].append((a,t,c))

q=collections.deque([(1,0,0,[1])])
while q:
    node,time,cost,visited=q.popleft()
    if node==N:
        answer=min(answer,cost)
        continue

    for n_node,n_time,n_cost in graph[node]:
        if time+n_time<=T and cost+n_cost<=M:
            if n_node not in visited:
                q.append((n_node,time+n_time,cost+n_cost,visited+[n_node]))

print(answer if answer!=sys.maxsize else -1)