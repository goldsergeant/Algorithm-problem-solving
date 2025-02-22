import collections
import sys

while True:
    N, M = sys.stdin.readline().split()
    N = int(N)
    M = float(M)
    M=int(M*100+0.5)
    if N == 0 and M == 0:
        break
    candies=[[0,0]]+[list(sys.stdin.readline().split()) for _ in range(N)]
    dp=collections.defaultdict(int)
    for i in range(1,N+1):
        candies[i][0]=int(candies[i][0])
        candies[i][1]=int(float(candies[i][1])*100+0.5)

    for i in range(1,N+1):
        for j in range(1,M+1):
            pre_cost=j-candies[i][1]
            if pre_cost>=0:
                dp[j]=max(dp[j],dp[pre_cost]+candies[i][0],dp[pre_cost]+candies[i][0])
            else:
                dp[j]=dp[j]

    print(dp[M])
