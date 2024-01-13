import collections
import sys

N,M=map(int,sys.stdin.readline().split())
graph=collections.defaultdict(list)
for _ in range(N-1):
    u,v,c=map(int,sys.stdin.readline().split())
    graph[u].append((v,c))
    graph[v].append((u,c))

def bfs(start,end):
    q=collections.deque([(start,0)])
    visited=[False]*(N+1)
    visited[start]=True
    while q:
        node,dist=q.popleft()
        if node==end:
            return dist
        
        for next_node,next_dist in graph[node]:
            if not visited[next_node]:
                visited[next_node]=True
                q.append((next_node,dist+next_dist))
                
for _ in range(M):
    a,b=map(int,sys.stdin.readline().split())
    print(bfs(a,b))