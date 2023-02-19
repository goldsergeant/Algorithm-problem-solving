import sys

n,k=map(int,sys.stdin.readline().split())
coins=[]
dp=[0 for i in range(k+1)]
for _ in range(n):
    coins.append(int(input()))
dp[0]=1
for i in range(n):
    for j in range(k+1):
        if j-coins[i]>=0:
            dp[j]+=dp[j-coins[i]]

print(dp[-1])
