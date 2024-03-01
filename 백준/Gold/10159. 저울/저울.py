import collections
import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
connected=[[False for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    connected[a][b]=True

for i in range(1,N+1):
    connected[i][i]=True

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if connected[i][k] and connected[k][j]:
                connected[i][j]=True

for i in range(1,N+1):
    cnt=0
    for j in range(1,N+1):
        if not connected[i][j] and not connected[j][i]:
            cnt+=1

    print(cnt)