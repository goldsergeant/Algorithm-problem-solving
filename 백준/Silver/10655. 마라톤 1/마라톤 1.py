import sys


def get_distance(a, b):
    x1, y1 = a
    x2, y2 = b
    return abs(x2 - x1) + abs(y2 - y1)


N=int(sys.stdin.readline())
check_points = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[sys.maxsize for _ in range(1+1)] for _ in range(len(check_points))]

dp[0][0]=0
for i in range(1,len(check_points)):
    dp[i][0]=dp[i-1][0]+get_distance(check_points[i-1], check_points[i])
    dp[i][1]=dp[i-1][1]+get_distance(check_points[i-1],check_points[i])
    if i-1>0:
        dp[i][1]=min(dp[i][1],dp[i-1-1][0]+get_distance(check_points[i-1-1],check_points[i]))

print(min(dp[-1]))