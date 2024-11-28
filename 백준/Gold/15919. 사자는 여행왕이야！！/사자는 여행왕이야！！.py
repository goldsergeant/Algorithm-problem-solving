import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
trips = [list(map(int, sys.stdin.readline().split())) for _ in range(M)] + [[N + 1, N + 1]]
trips.sort(key=lambda x: x[1])
answer = 0
dp=[sys.maxsize] * len(trips)
for i in range(len(trips)):
    dp[i] = trips[i][0] - 1
    for j in range(i - 1, -1, -1):
        if trips[i][0] > trips[j][1]:
            dp[i] = min(dp[i], max(dp[j],trips[i][0]-trips[j][1]-1))

print(dp[-1])
