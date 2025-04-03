import sys

def check(box):
    cnt = 0
    for start,end,space in rules:
        if box < start:
            continue

        cnt += (min(end, box) - start) // space + 1

    return cnt>=D

N,K,D=map(int,sys.stdin.readline().split())
rules=[]
total_acorn=0
for _ in range(K):
    start,end,space=map(int,sys.stdin.readline().split())
    rules.append([start,end,space])
    total_acorn+=(end-start)//space+1

left=1
right=N
while left+1<right:
    mid=(left+right)//2
    if check(mid):
        right=mid
    else:
        left=mid

print(right)