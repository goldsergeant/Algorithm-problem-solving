import sys

def check(mid):
    withdraw_cnt=0
    cur_money=0
    for money in monies:
        if money>mid:
            return False

        if cur_money<money:
            withdraw_cnt+=1
            cur_money=mid
        cur_money-=money
    return withdraw_cnt<=M

N,M=map(int,sys.stdin.readline().split())
monies=[int(sys.stdin.readline()) for _ in range(N)]

left=1
right=sum(monies)
while left+1<right:
    mid=(left+right)//2
    if check(mid):
        right=mid
    else:
        left=mid

print(right)