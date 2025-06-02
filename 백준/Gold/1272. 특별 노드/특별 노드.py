import collections
import sys
sys.setrecursionlimit(100000)

N, R = map(int, sys.stdin.readline().split())
weights = [0] + list(map(int, sys.stdin.readline().split()))
tree = collections.defaultdict(list)
graph=collections.defaultdict(list)
dp = [[[sys.maxsize, sys.maxsize] for _ in range(N + 1)] for _ in range(N + 1)]  # 노드,가까운 부모,[특별/비특별]
for _ in range(N - 1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

def set_tree():
    q=collections.deque([R])
    v=[False for _ in range(N + 1)]
    v[R]=True
    while q:
        node=q.popleft()

        for adj in graph[node]:
            if not v[adj]:
                v[adj]=True
                tree[node].append(adj)
                q.append(adj)

def dfs(cur, parent):
    if dp[cur][parent]!=[sys.maxsize,sys.maxsize]:
        return dp[cur][parent]
    dp[cur][parent][0] = weights[cur]
    dp[cur][parent][1] = weights[cur] - weights[parent]
    for child in tree[cur]:
        if weights[cur]>weights[parent]:
            special, not_special = dfs(child, cur)  # 현재 노드를 특별노드로 설정
            dp[cur][parent][0] += min(special, not_special)

        if cur!=R:
            special,not_special=dfs(child,parent)
            dp[cur][parent][1] += min(special, not_special)

    return dp[cur][parent][0], dp[cur][parent][1]

set_tree()
print(dfs(R, 0)[0])
