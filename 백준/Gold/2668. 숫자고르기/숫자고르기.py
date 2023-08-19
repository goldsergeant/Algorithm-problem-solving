import collections
import sys

n = int(sys.stdin.readline())
graph = collections.defaultdict(list)
visited=[False for _ in range(n+1)]
answer=[]
for i in range(1,n+1):
    graph[i].append(int(sys.stdin.readline()))

def dfs(u,target):
    for v in graph[u]:
        if v==target:
            answer.append(target)
            return
        if not visited[v]:
            visited[v]=True
            dfs(v,target)
            visited[v]=False

for i in range(1,n+1):
    visited[i]=True
    dfs(i,i)
    visited[i]=False

print(len(answer))
for num in answer:
    print(num)