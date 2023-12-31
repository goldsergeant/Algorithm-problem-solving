import sys

N,M=map(int,sys.stdin.readline().split())
memories=[0]+list(map(int,sys.stdin.readline().split()))
costs=[0]+list(map(int,sys.stdin.readline().split()))
total_cost=sum(costs)
dp=[[0 for _ in range(total_cost+1)] for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(total_cost+1):
        if j-costs[i]>=0:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-costs[i]]+memories[i])
        else:
            dp[i][j]=dp[i-1][j]

for j in range(total_cost+1):
    if list(filter(lambda x:x>=M,[dp[i][j] for i in range(1,N+1)])):
        print(j)
        exit()
