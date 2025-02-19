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

N = int(sys.stdin.readline())
planets = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
parent=[i for i in range(N)]
answer=0
for i in range(N):
    planets[i].append(i)

x_planets = sorted(planets, key=lambda x: x[0])
y_planets = sorted(planets, key=lambda x: x[1])
z_planets = sorted(planets, key=lambda x: x[2])
edges=[]

for i in range(N-1):
    x1=x_planets[i][0]
    x2=x_planets[i+1][0]
    x1_idx=x_planets[i][3]
    x2_idx=x_planets[i+1][3]
    y1=y_planets[i][1]
    y2=y_planets[i+1][1]
    y1_idx=y_planets[i][3]
    y2_idx=y_planets[i+1][3]
    z1=z_planets[i][2]
    z2=z_planets[i+1][2]
    z1_idx=z_planets[i][3]
    z2_idx=z_planets[i+1][3]

    edges.append((x2-x1,x1_idx,x2_idx))
    edges.append((y2-y1,y1_idx,y2_idx))
    edges.append((z2-z1,z2_idx,z1_idx))

edges.sort()
for cost,a,b in edges:
    a=find(a)
    b=find(b)
    if a!=b:
        union(a,b)
        answer+=cost

print(answer)