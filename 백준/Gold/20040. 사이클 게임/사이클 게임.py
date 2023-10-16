import sys
sys.setrecursionlimit(1000000)

n,m=map(int,sys.stdin.readline().split())
parent=[i for i in range(n)]
def find(x):
    if x!=parent[x]:
        parent[x]=find(parent[x])
        return parent[x]
    return x

def union(a,b):
    a=find(a)
    b=find(b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

for i in range(1,m+1):
    a,b=map(int,sys.stdin.readline().split())

    if i>=3 and find(a)==find(b):
        print(i)
        sys.exit()
    union(a,b)


print(0)