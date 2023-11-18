import collections
import sys

to_adult_day,stop_child_day,dead_day,n=map(int,sys.stdin.readline().split())
dp=[0 for _ in range(n+1)]
dp[0]=1
for i in range(1,n+1):
    dp[i]=dp[i-1]%1000
    if i-to_adult_day>=0:
        dp[i]+=dp[i-to_adult_day]%1000
    if i-stop_child_day>=0:
        dp[i]-=dp[i-stop_child_day]%1000

answer=dp[n]%1000
if n-dead_day>=0:
    answer-=dp[n-dead_day]
print(answer%1000)