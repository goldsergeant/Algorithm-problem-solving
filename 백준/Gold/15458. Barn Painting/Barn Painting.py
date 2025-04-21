import collections
import sys

sys.setrecursionlimit(10 ** 6)

N, K = map(int, sys.stdin.readline().split())
graph = collections.defaultdict(list)
colors = [0 for _ in range(N + 1)]
dp = [[0,0,0,0] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
MOD_NUM = 10 ** 9 + 7
for _ in range(N - 1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for _ in range(K):
    node, color = map(int, sys.stdin.readline().split())
    colors[node] = color


def dfs(node):
    visited[node] = True
    one, two, three = 1, 1, 1
    for next_node in graph[node]:
        if visited[next_node]:
            continue

        child_colors = dfs(next_node)
        one *= (child_colors[2] + child_colors[3]) % MOD_NUM
        two *= (child_colors[1] + child_colors[3]) % MOD_NUM
        three *= (child_colors[1] + child_colors[2]) % MOD_NUM

    if colors[node] == 0:
        dp[node][1] = one
        dp[node][2] = two
        dp[node][3] = three
    elif colors[node] == 1:
        dp[node][1] = one
        dp[node][2] = 0
        dp[node][3] = 0
    elif colors[node] == 2:
        dp[node][1] = 0
        dp[node][2] = two
        dp[node][3] = 0
    elif colors[node] == 3:
        dp[node][1] = 0
        dp[node][2] = 0
        dp[node][3] = three
    return dp[node]


print(sum(dfs(1)) % MOD_NUM)