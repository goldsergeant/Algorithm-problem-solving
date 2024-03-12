import collections
import sys

N=int(sys.stdin.readline())
scores=[0]*(N+1)
distance = [[sys.maxsize for _ in range(N+1)] for _ in range(N+1)]

while True:
    a,b=map(int,sys.stdin.readline().split())
    if a==-1 and b==-1:
        break
    distance[a][b]=1
    distance[b][a]=1

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if distance[i][j]>distance[i][k]+distance[k][j]:
                distance[i][j]=distance[i][k]+distance[k][j]

for i in range(1,N+1):
    distance[i][i]=sys.maxsize

for i,row in enumerate(distance):
    tmp=0
    for j in range(1,N+1):
        if i!=j and tmp<row[j]:
            tmp=row[j]
    scores[i]=tmp

min_score=min(scores)
print(min_score,scores.count(min_score))
for i in range(1,N+1):
    if scores[i]==min_score:
        print(i,end=' ')
