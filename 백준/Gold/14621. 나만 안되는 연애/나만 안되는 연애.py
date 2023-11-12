import collections
import sys
from heapq import heappush,heappop

n, m = map(int, sys.stdin.readline().split())
gender_school = [0] + list(sys.stdin.readline().split())
graph=collections.defaultdict(list)
for _ in range(m):
    u,v,d=map(int,sys.stdin.readline().split())
    if gender_school[u]!=gender_school[v]:
        graph[u].append((v,d))
        graph[v].append((u,d))


def prim():
    q=[(0,1)]
    visited=[False]*(n+1)
    total_distance=0

    while q:
        d,u=heappop(q)
        if not visited[u]:
            total_distance+=d
            visited[u]=True

            for v,d in graph[u]:
                if not visited[v] and gender_school[u]!=gender_school[v]:
                    heappush(q,(d,v))

    if all(visited[1:]):
        return total_distance
    else:
        return -1

print(prim())