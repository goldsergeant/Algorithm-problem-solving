import sys

n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
dp=[[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if arr[-i]!=arr[j-1]:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        else:
            dp[i][j]=dp[i-1][j-1]+1

print(n-dp[-1][-1])


