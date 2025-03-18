import collections
import sys

N, M, X = map(int, sys.stdin.readline().split())
graph1 = collections.defaultdict(list)
graph2 = collections.defaultdict(list)

behind_nodes = 0
front_nodes = 0


for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph1[b].append(a)
    graph2[a].append(b)

q1=collections.deque([X])
q2=collections.deque([X])

visited=[False for _ in range(N+1)]
visited[X]=True
while q1:
    node = q1.popleft()
    for n in graph1[node]:
        if not visited[n]:
            front_nodes += 1
            q1.append(n)
            visited[n]=True

visited=[False for _ in range(N+1)]
visited[X]=True
while q2:
    node=q2.popleft()
    for n in graph2[node]:
        if not visited[n]:
            behind_nodes += 1
            q2.append(n)
            visited[n]=True

print(1+front_nodes, N-behind_nodes)
