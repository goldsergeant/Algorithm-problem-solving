import collections
import sys


def dfs(node):
    if dp[node] != 0:
        return dp[node]

    for next_node in graph[node]:
        next_val=dfs(next_node)
        if next_val>dp[node]:
            dp[node]=next_val
        elif next_val==dp[node]:
            dp[node]=next_val+1

    dp[node]=max(1,dp[node])
    return dp[node]


T = int(sys.stdin.readline())
for _ in range(T):
    test_case, nodes_cnt, edges_cnt = map(int, sys.stdin.readline().split())
    graph = collections.defaultdict(list)
    in_degree = [0 for _ in range(nodes_cnt + 1)]
    dp = [0 for _ in range(nodes_cnt + 1)]
    for _ in range(edges_cnt):
        a, b = map(int, sys.stdin.readline().split())
        graph[b].append(a)
        in_degree[a] += 1

    root = 0
    for i in range(1, nodes_cnt + 1):
        if in_degree[i] == 0:
            root = i
            break

    print(f'{test_case} {dfs(root)}')