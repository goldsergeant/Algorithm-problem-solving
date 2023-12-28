import sys

N=int(sys.stdin.readline())
numbers=list(map(int,sys.stdin.readline().split()))
M=int(sys.stdin.readline())
dp = [[False for _ in range(N)] for _ in range(N)]

for j in range(N-1):
    if numbers[j]==numbers[j+1]:
        dp[j][j+1]=True
for i in range(N-1,-1,-1):
    dp[i][i]=True
    for j in range(i+2,N):
        dp[i][j]=(numbers[i]==numbers[j] and dp[i+1][j-1])


for _ in range(M):
    S,E=map(int,sys.stdin.readline().split())
    print(int(dp[S-1][E-1]))