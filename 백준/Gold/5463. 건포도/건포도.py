import sys

N, M = map(int, sys.stdin.readline().split())
chocolate =[[0]+list(map(int, sys.stdin.readline().split())) for _ in range(N)]
chocolate=[[0 for _ in range(M+1)]]+chocolate
t_sum = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
dp = [[[[-1 for _ in range(M + 1)] for _ in range(N + 1)] for _ in range(M + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        t_sum[i][j] = t_sum[i - 1][j] + t_sum[i][j - 1] - t_sum[i - 1][j - 1] + chocolate[i][j]


def dfs(s_r, s_c, e_r, e_c):
    if s_r == e_r and s_c == e_c:
        return 0
    if dp[s_r][s_c][e_r][e_c] != -1:
        return dp[s_r][s_c][e_r][e_c]

    dp[s_r][s_c][e_r][e_c] = sys.maxsize

    cur_sum = t_sum[e_r][e_c] - t_sum[s_r - 1][e_c] - t_sum[e_r][s_c - 1] + t_sum[s_r - 1][s_c - 1]

    for i in range(s_r, e_r):
        result1 = dfs(s_r, s_c, i, e_c)
        result2 = dfs(i + 1, s_c, e_r, e_c)
        dp[s_r][s_c][e_r][e_c] = min(dp[s_r][s_c][e_r][e_c], result1 + result2 + cur_sum)

    for i in range(s_c, e_c):
        result1 = dfs(s_r, s_c, e_r, i)
        result2 = dfs(s_r, i + 1, e_r, e_c)
        dp[s_r][s_c][e_r][e_c] = min(dp[s_r][s_c][e_r][e_c], result1 + result2 + cur_sum)

    return dp[s_r][s_c][e_r][e_c]


print(dfs(1, 1, N, M))
