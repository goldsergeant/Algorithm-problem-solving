import collections
import sys


N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
dp=[[-1 for _ in range(2+1)] for _ in range(N)]
dp[0][0]=0
for i in range(N-1): # 정방향
    if dp[i][0]==-1:
        continue
    next_position=i+numbers[i]
    if 0<=next_position<N:
        dp[next_position][0]=max(dp[next_position][0],dp[i][0]+1)

for i in range(N-2,-1,-1): # 역방향
    dp[i][1]=max(dp[i][0],dp[i][1])
    if dp[i][1]==-1:
        continue
    next_position=i-numbers[i]
    if 0<=next_position<N:
        dp[next_position][1]=max(dp[next_position][1],dp[i][1]+1)

for i in range(N-1): # 정방향
    dp[i][2]=max(dp[i][1],dp[i][2])

    if dp[i][2]==-1:
        continue
    next_position=i+numbers[i]
    if 0<=next_position<N:
        dp[next_position][2]=max(dp[next_position][2],dp[i][2]+1)

print(max(dp[N-1]))