import collections
import sys

m,n=map(int,sys.stdin.readline().split())
tomatos=[]
for _ in range(n):
    tomatos.append(list(map(int, sys.stdin.readline().split())))

queue=collections.deque()
for i in range(n):
    for j in range(m):
        if tomatos[i][j]==1:
            queue.append((i,j))

while queue:
    i,j=queue.popleft()
    if i>0 and tomatos[i-1][j]==0:
        queue.append((i-1,j))
        tomatos[i-1][j]=tomatos[i][j]+1
    if j>0 and tomatos[i][j-1]==0:
        queue.append((i,j-1))
        tomatos[i][j-1]=tomatos[i][j]+1
    if i<n-1 and tomatos[i+1][j]==0:
        queue.append((i+1,j))
        tomatos[i+1][j]=tomatos[i][j]+1
    if j<m-1 and tomatos[i][j+1]==0:
        queue.append((i,j+1))
        tomatos[i][j+1]=tomatos[i][j]+1

print(max(map(max,tomatos))-1 if all(0 not in l for l in tomatos) else -1)
