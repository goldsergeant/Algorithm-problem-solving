import sys

N = int(sys.stdin.readline())
distance=[[0 for _ in range(N+1)] for _ in range(N+1)]
result=[[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(1,N+1):
    nodes=[0]+list(map(int,sys.stdin.readline().split()))
    for j in range(1,N+1):
        distance[i][j]=nodes[j]
        result[i][j]=nodes[j]

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if k==i or k==j:
                continue
            if distance[i][k]+distance[k][j]<distance[i][j]:
                print(-1)
                exit()
            elif distance[i][k]+distance[k][j]==distance[i][j]:
                result[i][j]=0
total=0
for i in range(1,N+1):
    for j in range(1,N+1):
        total+=result[i][j]

print(total//2)