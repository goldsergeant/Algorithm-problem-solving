import sys

N,M=map(int,sys.stdin.readline().split())
distance=[[sys.maxsize for _ in range(N+1)] for _ in range(N+1)]
for i in range(1,N+1):
    distance[i][i]=0

for _ in range(M):
    a,b,t=map(int,sys.stdin.readline().split())
    distance[a][b]=t

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            distance[i][j]=min(distance[i][j],distance[i][k]+distance[k][j])

K=int(sys.stdin.readline())
friends=list(map(int,sys.stdin.readline().split()))
time=sys.maxsize
cities=[]

for x in range(1,N+1):
    tmp=0
    for f in friends:
        tmp=max(tmp,distance[f][x]+distance[x][f])
    if tmp==time:
        cities.append(x)
    elif tmp<time:
        time=tmp
        cities=[x]

print(*cities)