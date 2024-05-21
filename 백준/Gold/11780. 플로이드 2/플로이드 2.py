import sys

N=int(sys.stdin.readline())
M=int(sys.stdin.readline())
distance=[[sys.maxsize for _ in range(N+1)] for _ in range(N+1)]
path=[[-1 for i in range(N + 1)] for _ in range(N + 1)]

for _ in range(M):
    a,b,c=map(int,sys.stdin.readline().split())
    distance[a][b]=min(distance[a][b],c)
    path[a][b]=a

for i in range(1,N+1):
    distance[i][i]=0

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if distance[i][j]>distance[i][k]+distance[k][j]:
                distance[i][j]=distance[i][k]+distance[k][j]
                path[i][j]=path[k][j]

for i in range(1,N+1):
    for j in range(1,N+1):
        print(distance[i][j] if distance[i][j]!=sys.maxsize else 0,end=' ')
    print()

for i in range(1,N+1):
    for j in range(1,N+1):
        if path[i][j]==-1:
            print(0)
            continue

        cur=j
        cities=[]
        while cur!=i:
            cities.append(cur)
            cur=path[i][cur]
        print(len(cities)+1,i,*cities[::-1])