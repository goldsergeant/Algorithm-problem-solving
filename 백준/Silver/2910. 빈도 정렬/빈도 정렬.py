import collections
import sys

N,C=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))
counter=collections.Counter(arr)

print(*sorted(arr,key=lambda x:(counter[x],-arr.index(x)),reverse=True))