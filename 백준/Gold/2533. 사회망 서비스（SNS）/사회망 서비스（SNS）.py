import collections
import sys
sys.setrecursionlimit(1000000)

N = int(sys.stdin.readline())
NORMAL,EARLY_ADAPTER=0,1
dp=[[0,0] for _ in range(N+1)]
graph = collections.defaultdict(list)
visited = [False] * (N + 1)
for _ in range(N - 1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(node):
    visited[node]=True
    dp[node][NORMAL]=0
    dp[node][EARLY_ADAPTER]=1

    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node)
            dp[node][NORMAL]+=dp[next_node][EARLY_ADAPTER]
            dp[node][EARLY_ADAPTER]+=min(dp[next_node][NORMAL],dp[next_node][EARLY_ADAPTER])

dfs(1)
print(min(dp[1]))
