import collections
import sys
sys.setrecursionlimit(100000)

def solution(n, lighthouse):
    graph = collections.defaultdict(list)
    for a, b in lighthouse:
        graph[a].append(b)
        graph[b].append(a)
    dp = [[1, 0] for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]
    def dfs(node):
        visited[node] = True

        for next_node in graph[node]:
            if not visited[next_node]:
                on,off=dfs(next_node)
                dp[node][0]+=min(on,off)
                dp[node][1]+=on

        return dp[node][0],dp[node][1]

    visited = [False for _ in range(n + 1)]
    return min(dfs(1))


print(solution(8, [[1, 2], [1, 3], [1, 4], [1, 5], [5, 6], [5, 7], [5, 8]]))
print(solution(10, [[4, 1], [5, 1], [5, 6], [7, 6], [1, 2], [1, 3], [6, 8], [2, 9], [9, 10]]))
