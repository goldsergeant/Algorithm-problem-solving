import collections
import sys

n=int(input())
p=list(map(int,input().split()))
m=int(input())
dp=[0 for _ in range(m+1)]

for i in range(n-1,-1,-1):
    for j in range(p[i],m+1):
        dp[j]=max(dp[j],dp[j-p[i]]*10+i,i)

print(dp[m])