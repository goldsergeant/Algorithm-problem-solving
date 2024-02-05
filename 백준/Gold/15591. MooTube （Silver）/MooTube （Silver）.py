import collections
import sys

N, Q = map(int, sys.stdin.readline().split())
graph = collections.defaultdict(list)
for _ in range(N - 1):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def bfs(k, v):
    q = collections.deque([v])
    visited = [False for _ in range(N + 1)]
    visited[v] = True
    cnt = 0
    while q:
        node = q.popleft()

        for next_node, next_score in graph[node]:
            if not visited[next_node] and next_score >= k:
                visited[next_node] = True
                q.append(next_node)
                cnt += 1

    return cnt


for _ in range(Q):
    K, V = map(int, sys.stdin.readline().split())
    print(bfs(K, V))
