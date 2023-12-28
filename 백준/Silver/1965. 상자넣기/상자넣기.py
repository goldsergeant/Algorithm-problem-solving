import collections
import sys

N = int(sys.stdin.readline())
boxes=list(map(int,sys.stdin.readline().split()))
dp=[1]*(N+1)

for i in range(N-1):
    for j in range(i+1,N):
        if boxes[i]<boxes[j]:
            dp[j]=max(dp[j],dp[i]+1)


print(max(dp))