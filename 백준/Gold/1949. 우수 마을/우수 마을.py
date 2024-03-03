import collections
import sys
sys.setrecursionlimit(100000)

N = int(sys.stdin.readline())
scores = [0] + list(map(int, sys.stdin.readline().split()))
graph = collections.defaultdict(list)
visited = [False for _ in range(N + 1)]
dp = [[0, 0] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(node):
    visited[node] = True

    dp[node][1] = scores[node]
    for next_node in graph[node]:
        if not visited[next_node]:
            v1, v2 = dfs(next_node)
            dp[node][0] += max(v1, v2)
            dp[node][1] += v1

    return dp[node]


print(max(dfs(1)))

