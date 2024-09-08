import sys

G=int(sys.stdin.readline())
P=int(sys.stdin.readline())
airplanes=list(int(sys.stdin.readline()) for _ in range(P))
parent=[i for i in range(G+1)]
answer=0

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

for airplane in airplanes:
    airplane=find(airplane)
    if airplane==0:
        break
    answer+=1
    union(airplane,airplane-1)
print(answer)