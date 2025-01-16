import sys

N = int(sys.stdin.readline())
dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
dp[2][1]=2
for floor in range(3,N+1):
    for distance in range(1,floor):
        dp[floor][distance]=(dp[floor-1][distance]*2+dp[floor-1][distance-1]+dp[floor-1][distance+1])%10007

print(sum(dp[N])%10007)