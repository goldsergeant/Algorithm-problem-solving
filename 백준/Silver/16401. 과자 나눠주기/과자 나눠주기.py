import sys

M,N=map(int,sys.stdin.readline().split())
snacks=list(map(int,sys.stdin.readline().split()))
snacks.sort(reverse=True)

def is_possible(snacks,mid):
    cnt=0
    for snack in snacks:
        cnt+=(snack//mid)
        if cnt>=M:
            return True

    return False

left=1
right=snacks[0]
while left<=right:
    mid=(left+right)//2

    if is_possible(snacks,mid):
        left=mid+1
    else:
        right=mid-1

print(left-1)