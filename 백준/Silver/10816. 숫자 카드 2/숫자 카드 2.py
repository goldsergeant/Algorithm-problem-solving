import sys
from bisect import bisect_left,bisect_right

N=int(sys.stdin.readline())
cards=list(map(int,sys.stdin.readline().split()))
M=int(sys.stdin.readline())
targets=list(map(int,sys.stdin.readline().split()))

cards.sort()

for target in targets:
    cnt=bisect_right(cards,target)-bisect_left(cards,target)
    print(cnt,end=' ')