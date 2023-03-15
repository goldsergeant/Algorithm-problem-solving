import collections
import heapq
import sys

n, m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph.append((a,b,c))

distance = [sys.maxsize for _ in range(n + 1)]
distance[1] = 0

for i in range(1,n+1):
    for j in range(m):
        now,next,cost=graph[j][0],graph[j][1],graph[j][2]
        if distance[now]!=sys.maxsize and distance[next]>distance[now]+cost:
            distance[next]=distance[now]+cost
            if i==n:
                print(-1)
                exit()
for i in distance[2:]:
    print(i if i<sys.maxsize else -1)