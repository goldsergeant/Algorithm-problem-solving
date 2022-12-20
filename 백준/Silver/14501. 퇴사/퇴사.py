import collections
import sys

n = int(sys.stdin.readline())
counsel = []
pay = []
dp=[0 for i in range(n+1)]
profit=0

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    counsel.append(a)
    pay.append(b)

for i in range(n):
    profit = max(profit, dp[i])
    if i+counsel[i]>n:
        continue
    dp[i+counsel[i]]=max(profit+pay[i],dp[i+counsel[i]])
print(max(dp))