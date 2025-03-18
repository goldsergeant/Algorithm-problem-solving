import collections
import sys
sys.setrecursionlimit(100000+1)

N=int(sys.stdin.readline())
graph=collections.defaultdict(list)
for _ in range(N-1):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited=[False for _ in range(N+1)]
def dfs(node):
    visited[node]=True

    on,off=1,0
    for n in graph[node]:
        if not visited[n]:
            a,b=dfs(n)
            on+=min(a,b)
            off+=a

    return on,off

answer=0
for i in range(1,N+1):
    if not visited[i]:
        on,off=dfs(i)
        if min(on,off)==0:
            answer+=1
        else:
            answer+=min(on,off)

print(answer)