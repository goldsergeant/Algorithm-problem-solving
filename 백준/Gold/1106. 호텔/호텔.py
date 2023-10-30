import sys

c,n=map(int, sys.stdin.readline().split())
city_infos=[]
answer=[]
for _ in range(n):
    cost,num=map(int, sys.stdin.readline().split())
    city_infos.append((cost,num))

dp=[[sys.maxsize]*(c+1+100) for _ in range(n+1)]

dp[1][0]=0
for idx,city_info in enumerate(city_infos):
    cost,num=city_info
    for j in range(c+1+100):
        if j-num>=0:
            dp[idx+1][j]=min(dp[idx][j],dp[idx+1][j-num]+cost)
        else:
            dp[idx+1][j]=min(dp[idx+1][j],dp[idx][j])

print(min(dp[-1][c:]))