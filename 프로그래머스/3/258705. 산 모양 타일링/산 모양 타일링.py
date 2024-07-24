# dp[i][0] 옆 삼각형을 침범하지 않는 경우
# dp[i][1] 옆 삼각형을 침범하는 경우
def solution(n, tops):
    mod_num=10007
    dp=[[1 for _ in range(2)] for _ in range(n)] # 0이면 처음에 마름모 x 1이면 처음에 마름모
    if tops[0]==1:
        dp[0][0]=3
    else:
        dp[0][0]=2
    
    for i in range(1,n):
        dp[i][1]=(dp[i-1][0]+dp[i-1][1])%mod_num
        if tops[i]==1:
            dp[i][0]=(dp[i-1][0]*3+dp[i-1][1]*2)%mod_num
        else:
            dp[i][0]=(dp[i-1][0]*2+dp[i-1][1])%mod_num
    
    return sum(dp[-1])%mod_num