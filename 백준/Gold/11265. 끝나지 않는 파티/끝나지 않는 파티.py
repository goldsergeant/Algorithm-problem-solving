import sys

N,M=map(int,sys.stdin.readline().split())
distance=[[sys.maxsize for _ in range(N+1)] for _ in range(N+1)]
for i in range(1,N+1):
    arr=list(map(int,sys.stdin.readline().split()))
    for j in range(N):
        distance[i][j+1]=arr[j]

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            distance[i][j]=min(distance[i][j],distance[i][k]+distance[k][j])

for _ in range(M):
    a,b,c=map(int,sys.stdin.readline().split())
    if distance[a][b]<=c:
        print('Enjoy other party')
    else:
        print('Stay here')