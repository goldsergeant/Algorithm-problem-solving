import sys

st=sys.stdin.readline().rstrip()
dp=[[sys.maxsize,sys.maxsize] for _ in range(len(st))]
if st[0].islower():
    dp[0][0]=1
    dp[0][1]=2
else:
    dp[0][0]=2
    dp[0][1]=2

for i in range(1,len(st)):
    if st[i].islower():
        dp[i][0]=min(dp[i-1][0]+1,dp[i-1][1]+2)
        dp[i][1]=min(dp[i-1][0]+2,dp[i-1][1]+2)
    else:
        dp[i][0]=min(dp[i-1][0]+2,dp[i-1][1]+2)
        dp[i][1]=min(dp[i-1][0]+2,dp[i-1][1]+1)
print(min(dp[-1]))