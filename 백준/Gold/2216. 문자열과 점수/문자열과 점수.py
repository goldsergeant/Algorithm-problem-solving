import sys

A, B, C = map(int, sys.stdin.readline().split())
X = sys.stdin.readline().rstrip()
Y = sys.stdin.readline().rstrip()
dp = [[-sys.maxsize for _ in range(len(Y)+1)] for _ in range(len(X)+1)]

dp[0][0]=0
for i in range(len(X)+1):
    for j in range(len(Y)+1):
        if i<len(X) and j<len(Y):
            if X[i]==Y[j]:
                dp[i+1][j+1]=max(dp[i+1][j+1],dp[i][j]+A)
            else:
                dp[i+1][j+1]=max(dp[i+1][j+1],dp[i][j]+C)

        if i<len(X):
            dp[i+1][j]=max(dp[i+1][j],dp[i][j]+B)
        if j<len(Y):
            dp[i][j+1]=max(dp[i][j+1],dp[i][j]+B)

print(dp[-1][-1])