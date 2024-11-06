N,M=map(int,input().split())
times=list(int(input()) for _ in range(N))

left=1
right=max(times)*M

def check(val):
    cnt=0
    for time in times:
        cnt+=val//time

    return cnt>=M

while left+1<right:
    mid=(left+right)//2

    if check(mid):
        right=mid
    else:
        left=mid

print(right)