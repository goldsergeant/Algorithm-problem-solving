import sys

t=int(sys.stdin.readline().strip())
for _ in range(t):
    n=int(sys.stdin.readline().strip())
    stickers=[]
    stickers.append(list(map(int,sys.stdin.readline().split())))
    stickers.append(list(map(int,sys.stdin.readline().split())))
    dp=[[0 for _ in range(n)] for _ in range(2)]
    for i in range(n):
        if i==0:
            dp[0][0]=stickers[0][0]
            dp[1][0]=stickers[1][0]
        elif i==1:
            dp[0][1]=dp[1][0]+stickers[0][1]
            dp[1][1]=dp[0][0]+stickers[1][1]
        else:
            dp[0][i]=max(dp[1][i-1],max(dp[0][i-2],dp[1][i-2]))+stickers[0][i]
            dp[1][i]=max(dp[0][i-1],max(dp[0][i-2],dp[1][i-2]))+stickers[1][i]

    print(max(dp[0][n-1],dp[1][n-1]))