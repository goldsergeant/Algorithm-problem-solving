import sys

a1,a0=map(int,sys.stdin.readline().split())
c=int(input())
n0=int(input())
flag=0
for i in range(n0,101):
    if a1*i+a0>c*i:
        flag=1
print(0 if flag==1 else 1)