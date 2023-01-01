import sys

n=int(input())
houses=[]
dp=[[sys.maxsize for i in range(3)] for i in range(n)]

for i in range(n):
    houses.append(list(map(int,input().split())))

dp[0]=houses[0]

for y in range(1,n):
    for x in range(3):
        if x==0:
            dp[y][x]=min(dp[y-1][x+1],dp[y-1][x+2])+houses[y][x]
        if x==1:
            dp[y][x]=min(dp[y-1][x+1],dp[y-1][x-1])+houses[y][x]
        if x==2:
            dp[y][x]=min(dp[y-1][x-2],dp[y-1][x-1])+houses[y][x]

print(min(dp[n-1]))
