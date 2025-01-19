import math
import sys
sys.setrecursionlimit(10000)


def get_distance(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)


def dfs(n, m):
    next_task = max(n,m)+1
    if next_task == len(events):
        return 0
    if dp[n][m] != -1:
        return dp[n][m]

    case1=dfs(next_task,m)+get_distance(events[n][0],events[n][1],events[next_task][0],events[next_task][1])
    case2=dfs(n,next_task)+get_distance(events[m][0],events[m][1],events[next_task][0],events[next_task][1])
    if case1 < case2:
        dp_trace[n][m] = 1
        dp[n][m] = case1
    else:
        dp_trace[n][m] = 2
        dp[n][m] = case2

    return dp[n][m]


N = int(sys.stdin.readline())
W = int(sys.stdin.readline())
events = [[1, 1], [N, N]] + list(list(map(int, sys.stdin.readline().split())) for _ in range(W))
dp = [[-1 for _ in range(len(events))] for _ in range(len(events))]
dp_trace = [[0 for _ in range(len(events))] for _ in range(len(events))]

print(dfs(0,1))

n,m=0,1
for i in range(2,len(events)):
    print(dp_trace[n][m])
    if dp_trace[n][m] == 1:
        n=i
    else:
        m=i
