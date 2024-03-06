import collections
import itertools
import sys

N,M=map(int,sys.stdin.readline().split())
distance=[[sys.maxsize for _ in range(N+1)] for _ in range(N+1)]
answer=[]

for _ in range(M):
    a,b=map(int,sys.stdin.readline().split())
    distance[a][b]=1
    distance[b][a]=1

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            distance[i][j]=min(distance[i][j],distance[i][k]+distance[k][j])


for a,b in itertools.combinations([i for i in range(1,N+1)],2):
    total=0
    for i in range(1,N+1):
        if i!=a and i!=b:
            total+=min(distance[a][i],distance[b][i])

    answer.append((a,b,total*2))

print(*sorted(answer,key=lambda x:(x[2],x[0],x[1]))[0])