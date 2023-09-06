a=' '+input()
b=' '+input()
dp=[[0 for _ in range(len(b))] for _ in range(len(a))]

def is_diffrent(i,j):
    return a[i]!=b[j]

for i in range(len(b)):
    dp[0][i]=i

for i in range(len(a)):
    dp[i][0]=i

for i in range(1,len(a)):
    for j in range(1,len(b)):
        dp[i][j]=min(dp[i][j-1]+1,dp[i-1][j]+1,dp[i-1][j-1]+is_diffrent(i,j))

print(dp[-1][-1])