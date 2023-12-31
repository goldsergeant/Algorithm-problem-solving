import collections
import sys

N, M = map(int, sys.stdin.readline().split())
soldiers = [(0, 0)]
dp1 = [[0 for _ in range(N + 1)] for _ in range(N+1)]
dp2 = [[-sys.maxsize for _ in range(N+1)] for _ in range(M + 1)]


for _ in range(N):
    h, s = map(int, sys.stdin.readline().split())
    soldiers.append((h, s))

for i in range(1, N + 1):
    max_height=0
    total_strength=0
    for j in range(i, N + 1):
        height,strength=soldiers[j]
        if height>max_height:
            max_height=height
            total_strength=strength
        elif height==max_height:
            total_strength+=strength

        dp1[i][j]=total_strength

dp2[0][0]=0
for i in range(1, M + 1):
    for j in range(1, N + 1):
        for k in range(j):
            dp2[i][j] = max(dp2[i][j], dp2[i - 1][k] + dp1[k+1][j])

print(dp2[M][N])