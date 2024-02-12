import collections
import itertools
import sys
from heapq import heappush, heappop

N, K = map(int, sys.stdin.readline().split())
times = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
floid_graph = [[sys.maxsize for _ in range(N)] for _ in range(N)]
answer=sys.maxsize
for k in range(N):
    for i in range(N):
        for j in range(N):
            floid_graph[i][j]=min(floid_graph[i][j], times[i][k] + times[k][j])


for arr in itertools.permutations(i for i in range(N)):
    if arr[0]==K:
        temp=0
        for i in range(1,len(arr)):
            temp+=floid_graph[arr[i-1]][arr[i]]
        answer=min(answer,temp)

print(answer)