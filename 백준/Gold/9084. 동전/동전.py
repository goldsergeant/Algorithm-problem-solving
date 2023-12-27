import sys

T=int(sys.stdin.readline())
for _ in range(T):
    N=int(sys.stdin.readline())
    coins=[0]+list(map(int,sys.stdin.readline().split()))
    target=int(sys.stdin.readline())
    coins=list(filter(lambda x:x<=target,coins))
    dp=[[0]*(target+1) for _ in range(len(coins))]

    for i in range(1,len(coins)):
        dp[i][0]=1
        for j in range(1,target+1):
            dp[i][j]=dp[i-1][j]
            if j-coins[i]>=0:
                dp[i][j]+=dp[i][j-coins[i]]

    print(dp[-1][target])
