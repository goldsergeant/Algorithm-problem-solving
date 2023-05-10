import itertools
import sys

N,M=map(int,sys.stdin.readline().split())
arr=sorted(list(map(int,sys.stdin.readline().split())))
combi=itertools.combinations(arr,M)
for i in combi:
    print(*i)