import sys

N,M=map(int,sys.stdin.readline().split())
a=[]
b=[]
answer=0
for _ in range(N):
    a.append(list(map(int,sys.stdin.readline().strip())))

for _ in range(N):
    b.append(list(map(int, sys.stdin.readline().strip())))

def change(row, col):
    for i in range(row, row+3):
        for j in range(col, col+3):
          a[i][j] = 1 - a[i][j]

def check()->bool:
    for i in range(N):
        for j in range(M):
            if a[i][j]!=b[i][j]:
                return False
    return True

for i in range(N-2):
    for j in range(M-2):
        if a[i][j]!=b[i][j]:
            change(i,j)
            answer+=1

print(answer if check() else -1)


