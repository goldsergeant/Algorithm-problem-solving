import sys

T = int(sys.stdin.readline())


def dfs(i, j):
    if i == j:
        return 0
    if dp[i][j] != sys.maxsize:
        return dp[i][j]
    for m in range(i, j):
        dp[i][j] = min(dp[i][j], dfs(i, m) + dfs(m + 1, j))

    dp[i][j]+=t_sum[j]-t_sum[i-1]
    return dp[i][j]


for _ in range(T):
    N = int(sys.stdin.readline())
    files = [0]+list(map(int, sys.stdin.readline().split()))
    dp = [[sys.maxsize for _ in range(len(files))] for _ in range(len(files))]
    t_sum=[0]
    for i in range(1,len(files)):
        t_sum.append(t_sum[i-1]+files[i])
    print(dfs(1, N))
