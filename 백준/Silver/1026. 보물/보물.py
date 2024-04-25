import sys

N=int(sys.stdin.readline())
A=sorted(list(map(int,sys.stdin.readline().split())))
B=sorted(list(map(int,sys.stdin.readline().split())),reverse=True)
print(sum(a*b for a,b in zip(A,B)))