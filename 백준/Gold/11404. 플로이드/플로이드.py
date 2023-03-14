import collections
import heapq
import sys

n=int(input())
m=int(input())
graph= [[sys.maxsize for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    graph[a][b]=min(graph[a][b],c)
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==j:
                graph[i][j]=0
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

for i in range(1,n+1):
    for j in range(1,n+1):
        print(graph[i][j] if graph[i][j]<sys.maxsize else 0,end=' ')
    print()