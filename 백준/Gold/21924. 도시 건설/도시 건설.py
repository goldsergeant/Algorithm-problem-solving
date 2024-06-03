import sys
sys.setrecursionlimit(10**6)
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

N,M=map(int,sys.stdin.readline().split())
parent=[i for i in range(N+1)]
total_cost=0
edges=[]
for _ in range(M):
    a,b,c=map(int,sys.stdin.readline().split())
    total_cost+=c
    edges.append((a,b,c))
edges.sort(key=lambda x:x[2])
minimum_connected_cost=0

for a,b,c in edges:
    if find(a)!=find(b):
        union(a,b)
        minimum_connected_cost+=c

common_parent=find(1)
for i in range(2,N+1):
    if find(i)!=common_parent:
        print(-1)
        exit()

print(total_cost-minimum_connected_cost)