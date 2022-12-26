n,s,m=map(int,input().split())
volumes=list(map(int,input().split()))
dp=[[False]*(m+1) for _ in range(n+1)]
dp[0][s]=True
for i in range(n):
    for j in range(m+1):
        if dp[i][j]==False:
            continue
        if j-volumes[i]>=0:
            dp[i+1][j-volumes[i]]=True
        if j+volumes[i]<=m:
            dp[i+1][j+volumes[i]]=True
for i in range(m,-1,-1):
    if dp[n][i]==True:
        print(i)
        exit()
print(-1)