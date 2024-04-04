import sys

def divide(base,exp):
    if exp==0:
        return 1

    half=divide(base,exp//2)%C
    return half*half%C if exp%2==0 else half*half*base%C

A,B,C=map(int,sys.stdin.readline().split())
print(divide(A,B))