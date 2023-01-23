import sys

n,k=map(int,sys.stdin.readline().split())
coins=[]
coins_sum=0
count=0
for _ in range(n):
    coins.append(int(input()))

while True:
    mini=sys.maxsize
    choice_coin=0
    for i in range(len(coins)):
        if coins[i]>k:
            break
        if mini>k//coins[i] and i<len(coins)-1:
            mini=k//coins[i]
            choice_coin=coins[i]
            continue
        elif i==len(coins)-1:
            mini=k//coins[i]
            choice_coin=coins[i]
    k=k%choice_coin
    count+=mini

    if k==0:
        print(count)
        break