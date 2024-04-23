import sys

T=int(sys.stdin.readline())
for _ in range(T):
    N=int(sys.stdin.readline())
    coins=list(map(int,sys.stdin.readline().split()))
    target=int(sys.stdin.readline())
    dp=[[0 for _ in range(target+1)] for _ in range(N+1)]

    for i in range(1,N+1):
        dp[i][0]=1
        cur_coin=coins[i-1]
        for j in range(1,target+1):
            if j-cur_coin>=0:
                dp[i][j]=dp[i][j-cur_coin]+dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j]

    print(dp[N][target])