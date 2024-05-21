import sys

N=int(sys.stdin.readline())
M=int(sys.stdin.readline())
distance=[[sys.maxsize for _ in range(N+1)] for _ in range(N+1)]
route=[[[i] for i in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    a,b,c=map(int,sys.stdin.readline().split())
    distance[a][b]=min(distance[a][b],c)

for i in range(1,N+1):
    distance[i][i]=0

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if distance[i][j]>distance[i][k]+distance[k][j]:
                distance[i][j]=distance[i][k]+distance[k][j]
                route[i][j]=route[i][k]+route[k][j]

for i in range(1,N+1):
    for j in range(1,N+1):
        print(distance[i][j] if distance[i][j]!=sys.maxsize else 0,end=' ')
    print()

for i in range(1,N+1):
    for j in range(1,N+1):
        if i==j or distance[i][j]==sys.maxsize:
            print(0)
            continue

        print(len(route[i][j])+1,*([i]+route[i][j]))

