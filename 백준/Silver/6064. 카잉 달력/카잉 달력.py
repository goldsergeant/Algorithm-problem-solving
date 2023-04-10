import sys

t = int(input())
for _ in range(t):
    m, n, x, y = map(int, sys.stdin.readline().split())
    k = x
    flag=0
    while k<=m*n:
        if (k-y)%n==0:
            print(k)
            flag=1
            break
        k+=m
    if flag==0:
        print(-1)