import sys

n,k=map(int,sys.stdin.readline().split())
things=[[0,0]]
dp=[[0 for i in range(k+1)] for i in range(n+1)]
for i in range(n):
    w,v=map(int,sys.stdin.readline().split())
    things.append([w,v])

for i in range(1,n+1):
    for j in range(1,k+1):
        if j-things[i][0]>=0:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-things[i][0]]+things[i][1])
        else:
            dp[i][j]=dp[i-1][j]

answer=0
for i in range(1,n+1):
    answer=max(answer,max(dp[i]))

print(answer)

