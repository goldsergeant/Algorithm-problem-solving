import sys


def check(box_limit):
    cnt=0

    for start,end,space in rules:
        if box_limit<start:
            continue
        cnt+=(min(end,box_limit)-start)//space+1

    return cnt>=D

N,K,D=map(int,sys.stdin.readline().split())
rules=[list(map(int,sys.stdin.readline().split())) for _ in range(K)]

left=1
right=N

while left+1<right:
    mid=(left+right)//2

    if check(mid):
        right=mid
    else:
        left=mid

print(right)