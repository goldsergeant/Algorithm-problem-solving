import sys

H,W,X,Y=map(int,sys.stdin.readline().split())
B=[list(map(int,sys.stdin.readline().split())) for i in range(H+X)]

for i in range(H):
    for j in range(W):
        if i-X>=0 and j-Y>=0:
            B[i][j]-=B[i-X][j-Y]

for i in range(H):
    for j in range(W):
        print(B[i][j],end=" ")
    print()