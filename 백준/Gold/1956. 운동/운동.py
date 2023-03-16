import sys

v,e=map(int,sys.stdin.readline().split())
heap=[]
distance=[[sys.maxsize for _ in range(v+1)] for _ in range(v+1)]
for _ in range(e):
    a,b,c=map(int,sys.stdin.readline().split())
    distance[a][b]=c

for k in range(1,v+1):
    for i in range(1,v+1):
        for j in range(1,v+1):
            if distance[i][j]>distance[i][k]+distance[k][j]:
                distance[i][j]=distance[i][k]+distance[k][j]

answer=sys.maxsize
for i in range(1,v+1):
    answer=min(answer,distance[i][i])

print(answer if answer!=sys.maxsize else -1)
