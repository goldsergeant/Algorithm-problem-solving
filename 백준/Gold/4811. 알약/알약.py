import sys

def dfs(whole,half):
    if whole==0 and half==0:
        return 1
    if dp[whole][half]!=-1:
        return dp[whole][half]

    dp[whole][half]=0
    if whole>0:
        dp[whole][half]+=dfs(whole-1,half+1)
    if half>0:
        dp[whole][half]+=dfs(whole,half-1)

    return dp[whole][half]

while True:
    N=int(sys.stdin.readline())
    dp=[[-1 for _ in range(N+1)] for _ in range(N+1)]

    if N==0:
        break
    print(dfs(N,0))