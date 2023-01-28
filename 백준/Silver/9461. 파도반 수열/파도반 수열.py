dp=[0 for i in range(101)]
dp[1]=dp[2]=dp[3]=1
for i in range(4,101):
    dp[i]=dp[i-2]+dp[i-3]

t=int(input())
for i in range(t):
    print(dp[int(input())])