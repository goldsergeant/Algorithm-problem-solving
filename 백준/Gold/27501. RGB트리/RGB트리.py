import collections
import sys

sys.setrecursionlimit(1000000)


def dfs(parent, cur):
    dp[cur][0]=lights[cur][0]
    dp[cur][1]=lights[cur][1]
    dp[cur][2]=lights[cur][2]

    for child in graph[cur]:
        if child == parent:
            continue
        r, g, b = dfs(cur, child)
        dp[cur][R] += max(g, b)
        dp[cur][G] += max(r, b)
        dp[cur][B] += max(r,g)

    return dp[cur]


def trace_dp(parent, cur, parent_color):
    maximum = 0
    max_color = -sys.maxsize
    for i in range(2 + 1):
        if i == parent_color:
            continue
        if maximum < dp[cur][i]:
            max_color = i
            maximum = dp[cur][i]

    if max_color == R:
        answer_color[cur] = 'R'
    elif max_color == G:
        answer_color[cur] = 'G'
    elif max_color == B:
        answer_color[cur] = 'B'

    for child in graph[cur]:
        if child == parent:
            continue
        trace_dp(cur, child, max_color)


R = 0
G = 1
B = 2

N = int(sys.stdin.readline())
graph = collections.defaultdict(list)
dp = [[-1, -1, -1] for _ in range(N + 1)]
answer_color = ['' for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
lights = [[0, 0, 0]] + [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
print(max(dfs(-1, 1)))
trace_dp(-1, 1, -1)
for i in range(1,N+1):
    print(answer_color[i],end='')
