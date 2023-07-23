import sys

n = int(input())
students =list(map(int, sys.stdin.readline().split()))
dp = [0 for _ in range(n + 1)]
for i in range(n):
    dp[i+1]=dp[i]
    maxi=mini=students[i]
    j=i-1
    while j>=0 and (students[j]<mini or students[j]>maxi):
        mini,maxi=min(mini,students[j]),max(maxi,students[j]),
        dp[i+1]=max(dp[i+1],dp[j]+maxi-mini)
        j-=1

print(dp[-1])