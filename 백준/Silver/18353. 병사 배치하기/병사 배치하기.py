import sys

N=int(sys.stdin.readline())
numbers=list(map(int,sys.stdin.readline().split()))
dp=[1 for _ in range(N)]
for i in range(N):
    for j in range(i+1,N):
        if numbers[i]>numbers[j]:
            dp[j]=max(dp[j],dp[i]+1)

print(N-max(dp))