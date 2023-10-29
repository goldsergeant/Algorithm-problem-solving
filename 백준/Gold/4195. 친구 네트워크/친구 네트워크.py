import collections
import sys
input=sys.stdin.readline
t=int(input())
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
        network_count[a]=network_count.get(a,1)+network_count.get(b,1)
    elif a>b:
        parent[a]=b
        network_count[b]=network_count.get(a,1)+network_count.get(b,1)


for _ in range(t):
    f=int(input())
    parent=collections.defaultdict(str)
    network_count=dict()
    network_infos=[]
    keys=set()
    for _ in range(f):
        a,b=input().split()
        network_infos.append((a,b))
        keys.add(a)
        keys.add(b)

    for key in keys:
        parent[key]=key

    for a,b in network_infos:
        if find(a)!=find(b):
            union(a,b)
        print(network_count[find(a)])



