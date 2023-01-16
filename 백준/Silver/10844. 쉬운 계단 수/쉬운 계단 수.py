n=int(input())
dp=[[0 for i in range(10)] for i in range(n+1)]
dp[1]=[0,1,1,1,1,1,1,1,1,1]
for i in range(1,n):
    for j in range(10):
        if j==9:
            dp[i+1][j-1]+=dp[i][j]
        elif j==0 and i>1:
            dp[i+1][j+1]+=dp[i][j]
        elif j==0 and i==1:
            continue
        else:
            dp[i+1][j-1]+=dp[i][j]
            dp[i+1][j+1]+=dp[i][j]
print(sum(dp[n])%1000000000)
