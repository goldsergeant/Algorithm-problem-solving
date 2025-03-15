import sys


N = int(sys.stdin.readline())
customers = [0] + list(map(int, sys.stdin.readline().split()))
grab_cnt = int(sys.stdin.readline())
t_sum = [0 for _ in range(N + 1)]
answer = 0
dp=[[0 for _ in range(len(customers))] for _ in range(3+1)]
for i in range(1, len(t_sum)):
    t_sum[i] = t_sum[i - 1] + customers[i]

for i in range(1,3+1):
    for j in range(1,len(customers)-grab_cnt+1):
        dp[i][j]=max(dp[i][j-1],dp[i-1][j-grab_cnt]+t_sum[j+grab_cnt-1]-t_sum[j-1])

print(max(dp[3]))