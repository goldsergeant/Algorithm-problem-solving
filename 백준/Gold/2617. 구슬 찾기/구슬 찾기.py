import collections
import sys

N,M=map(int,sys.stdin.readline().split())
answer=0
heavy_graph=collections.defaultdict(list)
light_graph=collections.defaultdict(list)
for _ in range(M):
    a,b=map(int,sys.stdin.readline().split())
    heavy_graph[a].append(b)
    light_graph[b].append(a)


def dfs(node,graph):
    cnt=0
    visited[node]=True
    for next_node in graph[node]:
        if not visited[next_node]:
            cnt+=dfs(next_node,graph)+1
    return cnt

for i in range(1,N+1):
    visited=[False for _ in range(N+1)]
    if dfs(i,heavy_graph)>=(N+1)//2:
        answer+=1
    elif dfs(i,light_graph)>=(N+1)//2:
        answer+=1


print(answer)