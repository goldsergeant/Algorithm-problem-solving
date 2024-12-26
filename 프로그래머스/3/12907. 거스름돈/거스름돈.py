def solution(n, money):
    money=[0]+money
    dp=[[0 for _ in range(n+1)] for _ in range(len(money))]
    for i in range(len(money)):
        dp[i][0]=1
    
    for i in range(1,len(money)):
        for j in range(n+1):
            if j-money[i]>=0:
                dp[i][j]=dp[i-1][j]+dp[i][j-money[i]]
            else:
                dp[i][j]=dp[i-1][j]
    
    return dp[len(money)-1][n]