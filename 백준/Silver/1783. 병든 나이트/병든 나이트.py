import sys

N,M=map(int,sys.stdin.readline().split())
if N==1:
    print(1)
elif N<=2:
    print(min((M+1)//2,4))
elif M>=7:
    print(M-2)
else:
    print(min(4,M))