import collections
import math
import sys
N=int(sys.stdin.readline())
graph=collections.defaultdict(list)
for _ in range(N-1):
    a,b,p,q=map(int,sys.stdin.readline().split())
    graph[a].append((b,p,q))
    graph[b].append((a,q,p))

queue=collections.deque([0])
visited=[False for _ in range(N)]
visited[0]=True
denos=[0 for _ in range(N)]
numerators=[0 for _ in range(N)]
denos[0]=1
numerators[0]=1
while queue:
    now=queue.popleft()
    for adj,p,q in graph[now]:
        if not visited[adj]:
            visited[adj]=True
            d,n=denos[now],numerators[now]
            n_d=d*p
            n_n=n*q
            gc=math.gcd(n_d,n_n)
            n_d//=gc
            n_n//=gc
            denos[adj]=n_d
            numerators[adj]=n_n

            queue.append(adj)


lc=math.lcm(*denos)
print(*(numerators[i]*lc//denos[i] for i in range(N)))