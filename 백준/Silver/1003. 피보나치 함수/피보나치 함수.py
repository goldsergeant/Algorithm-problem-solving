t=int(input())
for _ in range(t):
    n = int(input())
    dp=[0]*(n+2)
    dp[n]=1
    for i in range(n,0,-1):
        if i>=2:
            dp[i-1]+=dp[i]
            dp[i-2]+=dp[i]
    print(dp[0],end=' ')
    print(dp[1])