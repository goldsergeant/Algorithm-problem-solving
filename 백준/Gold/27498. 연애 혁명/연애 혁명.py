import sys

def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

def union(a,b):
    a=find(a)
    b=find(b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

N,M=map(int,sys.stdin.readline().split())
parent=[i for i in range(N+1)]
edges=[[*map(int,sys.stdin.readline().split())] for _ in range(M)]
edges.sort(key=lambda x:(-x[3],-x[2]))
answer=0

for a,b,c,d in edges:
    if d==1:
        union(a,b)
    else:
        if find(a)!=find(b):
            union(a,b)
        else:
            answer+=c

print(answer)