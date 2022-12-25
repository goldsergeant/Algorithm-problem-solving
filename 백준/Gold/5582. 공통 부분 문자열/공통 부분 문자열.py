a=input()
b=input()
dp=[[0]*(len(b)+1) for _ in range(len(a)+1)]
answer=0
for i in range(len(a)):
    for j in range(len(b)):
        if a[i]==b[j]:
            dp[i][j]=dp[i-1][j-1]+1
            answer=max(answer,dp[i][j])
print(answer)
