import collections
import sys

n=int(sys.stdin.readline())
m=int(sys.stdin.readline())
parent=[i for i in range(n+1)]

def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
        return parent[x]
    return x

def union(a,b):
    a=find(a)
    b=find(b)
    if a!=b:
        if a<b:
            parent[b]=a
        else:
            parent[a]=b
for i in range(1,n+1):
    link_info=[0]+list(map(int,sys.stdin.readline().split()))
    for j in range(1,n+1):
        if link_info[j]==1:
            union(i,j)

plan=list(map(int,sys.stdin.readline().split()))
print('YES') if len(set(parent[i] for i in plan))==1 else print('NO')