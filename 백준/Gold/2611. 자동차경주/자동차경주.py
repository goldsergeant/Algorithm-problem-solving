import collections
import sys
from heapq import heappop,heappush

N=int(sys.stdin.readline())
M=int(sys.stdin.readline())
graph=collections.defaultdict(list)
path=[0 for _ in range(N+1)]

for _ in range(M):
    p,q,r=map(int,sys.stdin.readline().split())
    graph[p].append((q,r))

def bfs(start):
    distance=[-sys.maxsize for _ in range(N+1)]
    q=collections.deque([(start,0)])
    while q:
        node,cost=q.popleft()
        if cost<distance[node]:
            continue

        if node==1 and cost>0:
            continue

        for adj,adj_cost in graph[node]:
            n_cost=cost+adj_cost
            if n_cost>distance[adj]:
                distance[adj]=n_cost
                path[adj]=node
                q.append((adj,n_cost))

    return distance
visited_nodes=[]
cur=1
print(bfs(1)[1])

while True:
    visited_nodes.append(cur)
    cur=path[cur]
    if visited_nodes and cur==1:
        break

print(1,*visited_nodes[::-1])