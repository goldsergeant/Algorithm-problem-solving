import collections
import sys

n=int(sys.stdin.readline())
answer=0
dp=[0,0,1,1]
for i in range(4,n+1):
    if i%2==0:
        dp.append(dp[i-1]*2+1)
    else:
        dp.append(dp[i-1]*2-1)

print(dp[n])