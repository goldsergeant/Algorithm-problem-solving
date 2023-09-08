import sys

t=int(input())
k=int(input())
coins=[]
for _ in range(k):
    a,b=map(int,sys.stdin.readline().split())
    coins.append((a,b))

# coins.sort(reverse=True)
dp=[0 for _ in range(t+1)]
dp[0]=1
for coin in coins:
    price,cnt=coin
    for i in range(t,-1,-1):
        for j in range(1,cnt+1):
            if i-price*j>=0:
                dp[i]+=dp[i-price*j]

print(dp[t])

