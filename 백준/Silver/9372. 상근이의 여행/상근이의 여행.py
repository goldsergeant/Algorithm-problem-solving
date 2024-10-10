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

T=int(sys.stdin.readline())
for _ in range(T):
    N,M=map(int,sys.stdin.readline().split())
    parent=[i for i in range(N+1)]
    graph=[]
    for _ in range(M):
        a,b=map(int,sys.stdin.readline().split())
        graph.append((a,b))
    answer=0
    for a,b in graph:
        if find(a)!=find(b):
            answer+=1
            union(a,b)
    print(answer)