import sys

n = int(input())
cards = [0] + list(map(int, sys.stdin.readline().split()))
dp = [0]+[sys.maxsize for _ in range(n)]
for i in range(1, n + 1):
    for j in range(1,i+1):
        dp[i]=min(dp[i],dp[i-j]+cards[j])

print(dp[n])
