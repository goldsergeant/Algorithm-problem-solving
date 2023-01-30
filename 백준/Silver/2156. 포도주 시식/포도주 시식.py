n=int(input())
wine=[]
dp=[0 for i in range(n)]
for i in range(n):
    wine.append(int(input()))

dp[0]=wine[0]
for i in range(1,n):
    if i==1:
        dp[i]=wine[i]+wine[i-1]
    elif i==2:
        dp[i]=max(wine[i]+wine[i-1],wine[i]+wine[i-2],dp[i-1])
    else:
        dp[i]=max(dp[i-2]+wine[i],dp[i-3]+wine[i-1]+wine[i],dp[i-1])

print(dp[-1])

