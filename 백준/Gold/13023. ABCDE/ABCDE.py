import collections
import sys

N, M = map(int, sys.stdin.readline().split())
graph = collections.defaultdict(list)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(vertex, depth, visited):
    if depth == 5:
        print(1)
        exit()


    for node in graph[vertex]:
        if not visited[node]:
            visited[node] = True
            dfs(node, depth + 1, visited)
            visited[node] = False


for i in range(N):
    visited = [False for _ in range(N)]
    visited[i]=True
    dfs(i, 1, visited)

print(0)
