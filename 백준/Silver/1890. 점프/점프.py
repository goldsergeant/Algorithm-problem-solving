import collections
import sys

N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]


def solve():
    dp[0][0] = 1
    for i in range(N):
        for j in range(N):
            dist = board[i][j]
            if dist == 0:
                break
            for dy, dx in [(0, dist), (dist, 0)]:
                ny = i + dy
                nx = j + dx

                if 0 <= ny < N and 0 <= nx < N:
                    dp[ny][nx] += dp[i][j]
    return dp[-1][-1]

print(solve())