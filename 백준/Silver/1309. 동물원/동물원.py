n=int(input())
dp=[[0 for _ in range(3)] for _ in range(n+1)]  #0=공백 1=좌 2=우
mod_num=9901

dp[1][0]=dp[1][1]=dp[1][2]=1
for i in range(1,n):
    dp[i+1][0]=sum(dp[i])%mod_num
    dp[i+1][1]=dp[i][0]+dp[i][2]%mod_num
    dp[i+1][2]=dp[i][0]+dp[i][1]%mod_num

print(sum(dp[n])%mod_num)