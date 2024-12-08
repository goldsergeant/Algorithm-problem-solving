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

N=int(sys.stdin.readline())
edges=[]
total_cost=0

for i in range(1,N+1):
    arr=[0]+list(map(int,sys.stdin.readline().split()))
    for j in range(1,len(arr)):
        if i!=j:
            if arr[j]<0:
                total_cost-=arr[j]
            edges.append((i,j,arr[j]))


edges.sort(key=lambda x:x[2])
install_roads=[]
parent=[i for i in range(N+1)]
total_cost//=2

for a,b,c in edges:
    if find(a)!=find(b):
        union(a,b)
        if c>0:
            install_roads.append((a,b))
            total_cost+=c

print(total_cost,len(install_roads))
for arr in install_roads:
    print(*arr)