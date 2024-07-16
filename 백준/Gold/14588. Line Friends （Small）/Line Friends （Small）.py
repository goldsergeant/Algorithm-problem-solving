import collections
import sys

N = int(sys.stdin.readline())
lines = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
Q = int(sys.stdin.readline())

graph = collections.defaultdict(list)

for i in range(N):
    for j in range(N):
        x1, y1, x2, y2 = *lines[i], *lines[j]
        if x2<=x1<=y2 or x2<=y1<=y2 or x1<=x2<=y1 or x1<=y2<=y1:
            graph[i].append(j)
            graph[j].append(i)

for _ in range(Q):
    a, b = map(lambda x: int(x) - 1, sys.stdin.readline().split())
    visited=[sys.maxsize for _ in range(N)]
    q=collections.deque([a])
    visited[a]=0

    while q:
        node = q.popleft()
        for next_node in graph[node]:
            if visited[node]+1<visited[next_node]:
                visited[next_node]=visited[node]+1
                q.append(next_node)

    print(visited[b] if visited[b]!=sys.maxsize else -1)