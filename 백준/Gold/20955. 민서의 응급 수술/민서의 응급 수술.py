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
answer=0
for _ in range(M):
    u,v=map(int,sys.stdin.readline().split())
    if find(u)==find(v):
        answer+=1
    else:
        union(u,v)

root=1
for i in range(2,N+1):
    if find(i)!=root:
        answer+=1
        union(root,i)

print(answer)