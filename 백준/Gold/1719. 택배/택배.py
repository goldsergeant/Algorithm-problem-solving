import sys

N,M=map(int,sys.stdin.readline().split())
distance=[[sys.maxsize for _ in range(N+1)] for _ in range(N+1)]
routes=[[i for i in range(N+1)] for _ in range(N+1)]
for i in range(1,N+1):
    distance[i][i]=0
for _ in range(M):
    a,b,c=map(int,sys.stdin.readline().split())
    distance[a][b]=c
    routes[a][b]=b
    distance[b][a]=c
    routes[b][a]=a

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if distance[i][j]>distance[i][k]+distance[k][j]:
                distance[i][j]=distance[i][k]+distance[k][j]
                routes[i][j]=routes[i][k]

for i in range(1,N+1):
    for j in range(1,N+1):
        if i==j:
            print('-',end=' ')
        else:
            print(routes[i][j],end=' ')
    print()