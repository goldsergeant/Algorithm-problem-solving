import sys

def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]

def union(x,y):
    f_x=find(x)
    f_y=find(y)
    if f_x<f_y:
        parent[f_y]=f_x
    elif f_y<f_x:
        parent[f_x]=f_y

N,M,Q=map(int,sys.stdin.readline().split())
water_tanks=[0]+list(map(int,sys.stdin.readline().split()))
water_tanks=list(map(lambda x:-1 if x==0 else x,water_tanks))
parent=[i for i in range(N+1)]
for _ in range(M):
    u,v=map(int,sys.stdin.readline().split())
    union(u,v)

tmp_water_tanks=[0 for _ in range(N+1)]
for i in range(N+1):
    tmp_water_tanks[find(i)]+=water_tanks[i]

for _ in range(Q):
    K=int(sys.stdin.readline())
    print(1 if tmp_water_tanks[find(K)]>0 else 0)
