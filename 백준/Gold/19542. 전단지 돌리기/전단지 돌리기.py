import sys
sys.setrecursionlimit(100000)

N, S, D = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
dp = [1] * (N + 1)
answer = 0
for _ in range(N - 1):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(node):
    visited[node] = True
    for next_node in graph[node]:
        if not visited[next_node]:
            dp[node] = max(dp[node], dfs(next_node) + 1)
    return dp[node]


def get_dist(node,depth):
    global answer
    visited[node]=True
    flag=True
    for next_node in graph[node]:
        if not visited[next_node] and dp[next_node] > D:
            flag=False
            get_dist(next_node,depth+1)
    if flag:
        answer+=depth*2


visited = [False] * (N + 1)
dfs(S)
visited = [False] * (N + 1)
get_dist(S,0)
print(len(list(filter(lambda x:x!=S and visited[x],[i for i in range(1,N+1)])))*2)
