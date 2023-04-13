import collections
import itertools
import sys

n=int(input())
arr=collections.deque(map(int,sys.stdin.readline().split()))
answer=-sys.maxsize

def calc(arr):
    return_value=0
    for i in range(n-1):
        return_value+=abs(arr[i]-arr[i+1])

    return return_value

pe=list(itertools.permutations(arr,n))
for p in pe:
    answer=max(answer,calc(p))

print(answer)
