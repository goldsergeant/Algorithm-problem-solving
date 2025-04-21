import collections
import sys

sys.setrecursionlimit(10 ** 6)

N, K = map(int, sys.stdin.readline().split())
graph = collections.defaultdict(list)
colors = [0 for _ in range(N + 1)]
dp = [[-1, -1, -1, -1] for _ in range(N + 1)]
MOD_NUM = 10 ** 9 + 7
for _ in range(N - 1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for _ in range(K):
    node, color = map(int, sys.stdin.readline().split())
    colors[node] = color


def dfs(cur_node, cur_color, parent_node, parent_color):
    if cur_color == parent_color or (colors[cur_node] != 0 and cur_color != colors[cur_node]):
        return 0
    if dp[cur_node][cur_color] != -1:
        return dp[cur_node][cur_color]

    dp[cur_node][cur_color] = 1
    for child in graph[cur_node]:
        if child == parent_node:
            continue
        case = 0
        for c in range(1, 3 + 1):
            case += dfs(child, c, cur_node, cur_color)
            case %= MOD_NUM

        dp[cur_node][cur_color] *= case
        dp[cur_node][cur_color] %= MOD_NUM

    return dp[cur_node][cur_color]


print((dfs(1, 1, 0, 0) + dfs(1, 2, 0, 0) + dfs(1, 3, 0, 0)) % MOD_NUM)
