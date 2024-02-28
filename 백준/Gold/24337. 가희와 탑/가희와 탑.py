import sys

N,A,B=map(int,sys.stdin.readline().split())
buildings=[]
if N<(A+B)-1:
    print(-1)
    exit()

for i in range(A-1):
    buildings.append(i+1)

buildings.append(max(A,B))
for i in range(B-1):
    buildings.append((B-i-1))

print(buildings[0],end=' ')
for i in range(N-(A+B-1)):
    print(1,end=' ')

print(*buildings[1:])