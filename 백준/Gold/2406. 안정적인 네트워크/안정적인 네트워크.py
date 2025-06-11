import collections
import sys

def find(x):
    if x!=parent[x]:
        parent[x]=find(parent[x])

    return parent[x]

def union(x,y):
    x=find(x)
    y=find(y)
    if x<y:
        parent[y]=x
    else:
        parent[x]=y

N,M=map(int,sys.stdin.readline().split())
graph=collections.defaultdict(list)
edges=[]
parent=[i for i in range(N+1)]
for _ in range(M):
    a,b=map(int,sys.stdin.readline().split())
    edges.append((a,b,0))
    edges.append((b,a,0))

distance=[list(map(int,sys.stdin.readline().split())) for _ in range(N)]
for i in range(1,N):
    for j in range(1,N):
        edges.append((i+1,j+1,distance[i][j]))

edges.sort(key=lambda x:x[2])
cost=0
cnt=0
nodes=[]
for a,b,c in edges:
    if find(a)!=find(b):
        union(a,b)
        cost+=c
        if c>0:
            cnt+=1
            nodes.append(a)
            nodes.append(b)


print(cost,cnt)
print(*nodes)
