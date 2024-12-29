import sys


def get_distance(a, b):
    x1, y1 = a
    x2, y2 = b
    return abs(x2 - x1) + abs(y2 - y1)


N, K = map(int, sys.stdin.readline().split())
check_points = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[sys.maxsize for _ in range(K + 1)] for _ in range(len(check_points))]

dp[0][0] = 0
for i in range(1, len(check_points)):
    # dp[i][0] = dp[i - 1][0] + get_distance(check_points[i - 1], check_points[i])
    for j in range(K+1):
        if i-j<=0:
            continue
        for k in range(j+1):
            dp[i][j]=min(dp[i][j],dp[i-k-1][j-k]+get_distance(check_points[i-k-1], check_points[i]))
# for arr in dp:
#     print(arr)

print(min(dp[-1]))
