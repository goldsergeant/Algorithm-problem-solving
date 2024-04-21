import sys

N, K = map(int, sys.stdin.readline().split())
gallery = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[[-1 for _ in range(3)] for _ in range(K + 1)] for _ in range(N)]  # [행][몇개방닫][방닫상태]
LEFT_CLOSED = 0
RIGHT_CLOSED = 1
ALL_OPENED = 2


def get_rest_sum(line):
    total = 0
    for i in range(line, N):
        total += gallery[i][0] + gallery[i][1]
    return total


def dfs(line, close_cnt, state):
    if close_cnt==K:
        return get_rest_sum(line)
    if line==N:
        return -sys.maxsize
    if dp[line][close_cnt][state]!=-1:
        return dp[line][close_cnt][state]

    dp[line][close_cnt][state] = -sys.maxsize

    if state != LEFT_CLOSED:
        dp[line][close_cnt][state] = max(dp[line][close_cnt][state],
                                         dfs(line + 1, close_cnt + 1, RIGHT_CLOSED) + gallery[line][0])
    if state != RIGHT_CLOSED:
        dp[line][close_cnt][state] = max(dp[line][close_cnt][state],
                                         dfs(line + 1, close_cnt + 1, LEFT_CLOSED) + gallery[line][1])
    dp[line][close_cnt][state] = max(dp[line][close_cnt][state],
                                     dfs(line + 1, close_cnt, ALL_OPENED) + gallery[line][0] + gallery[line][1])
    return dp[line][close_cnt][state]


print(dfs(0, 0, ALL_OPENED))
