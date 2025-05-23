import itertools
import sys

MOD_NUM = 10 ** 9 + 7


def dfs(s, d, k, h):
    if s == S:
        if d==D and k==K and h==H:
            return 1
        return 0
    if dp[s][d][k][h] != -1:
        return dp[s][d][k][h]

    dp[s][d][k][h] = 0

    if d < D:
        dp[s][d][k][h] += dfs(s + 1, d + 1, k, h)
    if k < K:
        dp[s][d][k][h] += dfs(s + 1, d, k + 1, h)
    if h < H:
        dp[s][d][k][h] += dfs(s + 1, d, k, h + 1)

    if d < D and k < K:
        dp[s][d][k][h] += dfs(s + 1, d + 1, k + 1, h)
    if d < D and h < H:
        dp[s][d][k][h] += dfs(s + 1, d + 1, k, h + 1)
    if k < K and h < H:
        dp[s][d][k][h] += dfs(s + 1, d, k + 1, h + 1)

    if d < D and k < K and h < H:
        dp[s][d][k][h] += dfs(s + 1, d + 1, k + 1, h + 1)

    dp[s][d][k][h]%=MOD_NUM
    return dp[s][d][k][h]


S, D, K, H = map(int, sys.stdin.readline().split())
dp = [[[[-1 for _ in range(H + 1)] for _ in range(K + 1)] for _ in range(D + 1)] for _ in range(S)]  # s,d,k,h
print(dfs(0, 0, 0, 0))
