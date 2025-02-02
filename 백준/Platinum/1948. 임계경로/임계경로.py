import collections
import sys
from functools import cache
sys.setrecursionlimit(100000)

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = collections.defaultdict(list)
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[b].append((a, c))

start, end = map(int, sys.stdin.readline().split())
dp = [-1 for _ in range(N + 1)]
pre = [[] for _ in range(N + 1)]


def dfs(node):
    if node == start:
        return 0
    if dp[node] != -1:
        return dp[node]

    dp[node] = 0
    for next_node, next_cost in graph[node]:
        cur_cost = dfs(next_node) + next_cost
        if cur_cost > dp[node]:
            dp[node] = cur_cost
            pre[node] = [next_node]
        elif cur_cost == dp[node]:
            pre[node].append(next_node)

    return dp[node]


print(dfs(end))
path_cnt=0
q=collections.deque([end])
visited=[False for _ in range(N + 1)]
visited[end] = True

while q:
    node = q.popleft()
    path_cnt+=len(pre[node])
    for next_node in pre[node]:
        if not visited[next_node]:
            visited[next_node] = True
            q.append(next_node)

print(path_cnt)