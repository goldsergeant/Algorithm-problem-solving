import collections
import sys

N,P,Q=map(int,sys.stdin.readline().split())
dp=collections.defaultdict(int)
dp[0]=1

def dfs(num):
    if dp[num]==0:
        dp[num]=dfs(num//P)+dfs(num//Q)

    return dp[num]

print(dfs(N))