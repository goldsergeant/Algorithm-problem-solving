import sys
sys.setrecursionlimit(1000000)
n = 0
answer = 0
dp = [[-1 for _ in range(2)] for _ in range(1000000+1)]
moneys=None



def dfs(idx, first_selected):
    global n,moneys
    if idx >= n:
        return 0
    if first_selected and idx == n - 1:
        return 0
    if dp[idx][first_selected] != -1:
        return dp[idx][first_selected]

    dp[idx][first_selected] = 0
    dp[idx][first_selected] = max(dp[idx][first_selected], dfs(idx + 2, first_selected) + moneys[idx],
                                dfs(idx + 1, first_selected))
    return dp[idx][first_selected]


def solution(money):
    global n,moneys
    n = len(money)
    moneys=money
    return max(dfs(0, True), dfs(1, False))