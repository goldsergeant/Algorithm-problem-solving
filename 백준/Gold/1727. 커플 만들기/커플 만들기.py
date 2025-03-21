import sys

N, M = map(int, sys.stdin.readline().split())
men = [0]+list(map(int, sys.stdin.readline().split()))
women = [0]+list(map(int, sys.stdin.readline().split()))
dp=[[sys.maxsize for _ in range(len(women))] for _ in range(len(men))]
men.sort()
women.sort()
for i in range(len(men)):
    dp[i][0]=0
for i in range(len(women)):
    dp[0][i]=0

for i in range(1,len(men)):
    for j in range(1,len(women)):
        if i==j:
            dp[i][j]=dp[i-1][j-1]+abs(men[i]-women[i])
        elif i<j:
            dp[i][j]=min(dp[i][j-1],dp[i-1][j-1]+abs(men[i]-women[j]))
        else:
            dp[i][j]=min(dp[i-1][j],dp[i-1][j-1]+abs(men[i]-women[j]))

print(dp[-1][-1])