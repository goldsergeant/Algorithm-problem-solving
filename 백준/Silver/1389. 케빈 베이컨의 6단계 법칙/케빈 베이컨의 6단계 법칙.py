import collections
import sys

n,m=map(int,sys.stdin.readline().split())
graph=collections.defaultdict(list)
distance=[[sys.maxsize for _ in range(n+1)] for _ in range(n+1)]
answer=[]

for i in range(1,n+1):
    distance[i][i]=0

for _ in range(m):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    distance[a][b]=1
    distance[b][a]=1

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            distance[i][j]=min(distance[i][j],distance[i][k]+distance[k][j])

num=sys.maxsize
for i in range(1,n+1):
    tmp=sum(distance[i][1:])
    answer.append((tmp,i))

print(sorted(answer)[0][1])