import collections
import sys

N, M = map(int, sys.stdin.readline().split())
graph = collections.defaultdict(list)
level = [0 for i in range(N + 1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[b].append(a)


def dfs(x):
    if level[x] == 0:
        level[x] = max([dfs(next_x) for next_x in graph[x]], default=0) + 1
    return level[x]

for i in range(1,N+1):
    if level[i]==0:
        dfs(i)

print(*level[1:])