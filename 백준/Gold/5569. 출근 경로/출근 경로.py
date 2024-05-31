import sys

MOD_NUM = 100000

W, H = map(int, sys.stdin.readline().split())
dp = [[[0  for _ in range(4)] for _ in range(H + 1)] for _ in range(W + 1)]  # w,h,dw,dh
BOTTOM_BOTTOM=0
RIGHT_BOTTOM=1
RIGHT_RIGHT=2
BOTTOM_RIGHT=3

for i in range(1, W + 1):
    dp[i][1][RIGHT_RIGHT]=1
for i in range(1,H+1):
    dp[1][i][BOTTOM_BOTTOM]=1
for w in range(2,W+1):
    for h in range(2,H+1):
        dp[w][h][BOTTOM_BOTTOM]=(dp[w][h-1][RIGHT_BOTTOM]+dp[w][h-1][BOTTOM_BOTTOM])%MOD_NUM
        dp[w][h][RIGHT_BOTTOM]=dp[w][h-1][RIGHT_RIGHT]%MOD_NUM
        dp[w][h][RIGHT_RIGHT]=(dp[w-1][h][RIGHT_RIGHT]+dp[w-1][h][BOTTOM_RIGHT])%MOD_NUM
        dp[w][h][BOTTOM_RIGHT]=dp[w-1][h][BOTTOM_BOTTOM]%MOD_NUM

print(sum(dp[W][H])%MOD_NUM)

