t = int(input())
dp = [0,1,2,4]
length=4
for _ in range(t):
    n = int(input())
    while length<=n:
        dp.append((dp[length-1]+dp[length-2]+dp[length-3])%1000000009)
        length+=1
    print(dp[n]%1000000009)