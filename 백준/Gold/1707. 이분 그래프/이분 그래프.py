import collections
import sys

k = int(sys.stdin.readline())


def bfs(graph, start):
    queue = collections.deque()
    queue.append(start)
    if colors[start] is None:
        colors[start] = "RED"
    while queue:
        node = queue.popleft()
        for next in graph[node]:
            if colors[next] is None:
                colors[next] = "BLUE" if colors[node] == "RED" else "RED"
                queue.append(next)

            else:
                if colors[node] == colors[next]:
                    print("NO")
                    return False

    return True


for _ in range(k):
    v, e = map(int, sys.stdin.readline().split())
    graph = collections.defaultdict(list)
    colors = [None for i in range(v + 1)]
    flag = 0

    for _ in range(e):
        u, v1 = map(int, sys.stdin.readline().split())
        graph[u].append(v1)
        graph[v1].append(u)

    for i in range(1, v + 1):
        if not bfs(graph, i):
            flag = 1
            break

    if flag == 0:
        print("YES")
