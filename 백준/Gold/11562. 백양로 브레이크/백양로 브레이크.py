import sys

N,M=map(int,sys.stdin.readline().split())
distance=[[sys.maxsize for _ in range(N+1)] for _ in range(N+1)]
for i in range(1,N+1):
    distance[i][i]=0
for _ in range(M):
    u,v,b=map(int,sys.stdin.readline().split())
    if b==1:
        distance[u][v]=0
        distance[v][u]=0
    else:
        distance[u][v]=0
        distance[v][u]=1

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            distance[i][j]=min(distance[i][j],distance[i][k]+distance[k][j])

K=int(sys.stdin.readline())
for _ in range(K):
    s,e=map(int,sys.stdin.readline().split())
    print(distance[s][e])