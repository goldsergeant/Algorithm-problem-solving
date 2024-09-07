import sys
from heapq import heappush, heappop

N = int(sys.stdin.readline())
graph = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
answer=0
heap=[]
for i in range(1, N + 1):
    graph[i][i] = 0
    heappush(heap,(int(sys.stdin.readline().strip()), i))

for i in range(N):
    arr = list(map(int, sys.stdin.readline().split()))
    for j in range(len(arr)):
        if i!=j:
            graph[i+1][j+1] = arr[j]

visited=[False for _ in range(N+1)]

while heap:
    cost,node=heappop(heap)
    if visited[node]:
        continue

    visited[node]=True
    answer+=cost

    for j in range(1,len(graph[node])):
        if visited[j]:
            continue
        heappush(heap,(graph[node][j],j))

print(answer)