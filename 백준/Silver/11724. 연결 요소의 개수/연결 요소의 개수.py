import collections
import sys

N,M=map(int,sys.stdin.readline().split())
graph=collections.defaultdict(list)
visited = [False for _ in range(N + 1)]
answer=0

for _ in range(M):
    u,v=map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(start):
    queue=collections.deque()
    queue.append(start)
    visited[start]=True
    while queue:
        u=queue.popleft()
        for v in graph[u]:
            if not visited[v]:
                visited[v]=True
                queue.append(v)

for i in range(1,N+1):
    if not visited[i]:
        bfs(i)
        answer+=1


print(answer)