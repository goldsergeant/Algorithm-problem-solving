import collections
import sys



N=int(sys.stdin.readline())
start,end=map(int,sys.stdin.readline().split())
M=int(sys.stdin.readline())
graph=collections.defaultdict(list)
for _ in range(M):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

q=collections.deque([(start,0)])
visited=[False for _ in range(N+1)]
visited[start]=True
while q:
    node,dist=q.popleft()
    if node==end:
        print(dist)
        exit()

    for next_node in graph[node]:
        if not visited[next_node]:
            visited[next_node]=True
            q.append((next_node,dist+1))

print(-1)