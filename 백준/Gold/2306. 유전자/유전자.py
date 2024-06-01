import sys


def dfs(left, right):
    if left >= right:
        return 0
    if dp[left][right] != -1:
        return dp[left][right]

    dp[left][right] = 0
    if (st[left], st[right]) == ('a', 't') or (st[left], st[right]) == ('g', 'c'):
        dp[left][right] = dfs(left + 1, right - 1) + 2

    for i in range(left, right+1):
        dp[left][right] = max(dp[left][right], dfs(left, i) + dfs(i + 1, right))

    return dp[left][right]


st = sys.stdin.readline().rstrip()
dp = [[-1 for _ in range(len(st))] for _ in range(len(st))]
print(dfs(0, len(st) - 1))
