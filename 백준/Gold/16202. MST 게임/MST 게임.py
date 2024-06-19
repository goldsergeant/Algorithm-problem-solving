import collections
import sys

def find(x):
    if x!=parent[x]:
        parent[x]=find(parent[x])
    return parent[x]

def union(a,b):
    a=find(a)
    b=find(b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b


N,M,K=map(int,sys.stdin.readline().split())
edges=[]
parent=[i for i in range(N+1)]
for i in range(M):
    x,y=map(int,sys.stdin.readline().split())
    edges.append((x,y,i+1))

for k in range(K):
    cost=0
    parent=[i for i in range(N+1)]
    for x,y,c in edges:
        x=find(x)
        y=find(y)
        if x!=y:
            union(x,y)
            cost+=c

    nodes=set()
    for i in range(1,N+1):
        nodes.add(find(i))
    if len(nodes)==1:
        print(cost,end=' ')
    else:
        print(' '.join('0'*(K-k)))
        exit()

    edges.pop(0)