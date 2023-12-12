import collections
import sys

N, M = map(int, sys.stdin.readline().split())
parent = [[] for _ in range(N + 1)]
in_degree = [0] * (N + 1)
answer = collections.deque()

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    parent[b].append(a)
    in_degree[a] += 1


def topology():
    q = collections.deque()

    for i in range(1, N + 1):
        if in_degree[i] == 0:
            q.append(i)

    while q:
        node = q.popleft()
        answer.append(node)
        for parent_node in parent[node]:
            in_degree[parent_node] -= 1
            if in_degree[parent_node]==0:
                q.appendleft(parent_node)

topology()
print(*reversed(answer))
