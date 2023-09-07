import sys
from math import comb

while True:
    n,k=map(int,sys.stdin.readline().split())
    if n==0 and k==0:
        break

    print(comb(n,k))
