import collections
import sys

N = int(sys.stdin.readline())
weights = [0] + list(map(int, sys.stdin.readline().split()))
graph = collections.defaultdict(list)
visited=[False for _ in range(N+1)]
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

dp = [[0, 0] for _ in range(N + 1)]  # 현재 노드를 포함시킬때, 안포함시킬때


def dfs(node):
    visited[node] = True
    dp[node][0]=weights[node]

    for next_node in graph[node]:
        if not visited[next_node]:
            n_dp = dfs(next_node)
            dp[node][0] += n_dp[1]
            if n_dp[0]>n_dp[1]:
                dp[node][1] += n_dp[0]
            else:
                dp[node][1] += n_dp[1]

    return dp[node][0], dp[node][1]

print(max(dfs(1)))
nodes=[]
is_selected=[False for _ in range(N+1)]

def dfs(cur,prev):
    if dp[cur][0]>dp[cur][1] and not is_selected[prev]:
        nodes.append(cur)
        is_selected[cur]=True

    for next_node in graph[cur]:
        if next_node!=prev:
            dfs(next_node,cur)

dfs(1,0)
print(*sorted(nodes))