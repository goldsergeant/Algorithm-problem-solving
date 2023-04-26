import itertools
import sys

N,M=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))
arr.sort()
answer_arr=list(itertools.permutations(arr,M))
for i in answer_arr:
    print(*i)