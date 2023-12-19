import sys

N=int(sys.stdin.readline())
M=int(sys.stdin.readline())
fixed_seats=[int(sys.stdin.readline()) for _ in range(M)]
dp=[1]*(N+1)

for i in range(2,N+1):
    if i not in fixed_seats and i-1 not in fixed_seats:
        dp[i]=dp[i-1]+dp[i-2]
    else:
        dp[i]=dp[i-1]

print(dp[-1])