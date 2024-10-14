import collections
import sys
sys.setrecursionlimit(1000000)

N=int(sys.stdin.readline())
connected_cnt=[0 for _ in range(N + 1)]
graph=collections.defaultdict(list)
visited=[False for _ in range(N+1)]
for _ in range(N-1):
    u,v=map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

dp=[[0 for _ in range(2)] for _ in range(N+1)] # node,설치여부

def dfs(node):
    visited[node]=True
    tmp_f=0
    tmp_t=1
    for next_node in graph[node]:
        if not visited[next_node]:
            n_f,n_t=dfs(next_node)
            tmp_f+=n_t
            tmp_t+=min(n_f,n_t)

    dp[node][False]=tmp_f
    dp[node][True]=max(tmp_t,1)
    # print(f'return {node} : {dp[node]}')
    return dp[node]

# print(min(dfs(1)))

print(min(dfs(1)))
