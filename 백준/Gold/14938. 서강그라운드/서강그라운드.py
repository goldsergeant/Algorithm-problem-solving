import collections
import sys

def bfs(start):
    q=collections.deque([(0,start)])
    visited=[False for _ in range(N+1)]
    visited[start]=True
    item=0
    while q:
        cost,node=q.popleft()
        item+=items[node]
        for next_node in range(1,N+1):
            if cost+distance[node][next_node]<=M and not visited[next_node]:
                visited[next_node]=True
                q.append((cost+distance[node][next_node],next_node))
    return item

N,M,R=map(int,sys.stdin.readline().split())
items=[0]+list(map(int,sys.stdin.readline().split()))
distance=[[sys.maxsize for _ in range(N+1)] for _ in range(N+1)]
answer=0
for i in range(N+1):
    distance[i][i]=0

for _ in range(R):
    a,b,l=map(int,sys.stdin.readline().split())
    distance[a][b]=min(distance[a][b],l)
    distance[b][a]=min(distance[b][a],l)

for k in range(1,N+1):
    for i in range(N+1):
        for j in range(N+1):
            distance[i][j]=min(distance[i][j],distance[i][k]+distance[k][j])

for i in range(1,N+1):
    answer=max(answer,bfs(i))

print(answer)