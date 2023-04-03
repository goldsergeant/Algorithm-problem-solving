import sys

n=int(input())
numbers=list(map(int,sys.stdin.readline().split()))
answer=-sys.maxsize
dp = [[0] * n for _ in range(2)]
dp[0][0]=numbers[0]

if n==1:
    print(dp[0][0])
else:
    for i in range(1,n):
        dp[0][i]=max(dp[0][i-1]+numbers[i],numbers[i])
        dp[1][i]=max(dp[1][i-1]+numbers[i],dp[0][i-1])
        answer=max(answer,dp[0][i],dp[1][i])

    print(answer)