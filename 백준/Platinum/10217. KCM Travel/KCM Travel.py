import collections
import sys


def dijkstra():
    heap = collections.deque([(0, 0, 1)])
    distance = [[sys.maxsize for _ in range(M + 1)] for _ in range(N + 1)]
    distance[1][0] = 0
    while heap:
        duration, cost, node = heap.popleft()
        if duration > distance[node][cost]:
            continue

        if node == N:
            continue

        for next_node, next_cost, next_duration in graph[node]:
            ndist=distance[node][cost]+next_duration
            if cost + next_cost <= M and ndist < distance[next_node][cost + next_cost]:
                for c in range(cost + next_cost, M + 1):
                    if ndist<distance[next_node][c]:
                        distance[next_node][c] = ndist
                    else:
                        break
                # distance[next_node][cost + next_cost] =  ndist
                heap.append((ndist, cost + next_cost, next_node))

    ans=min(distance[N])
    return ans if ans!=sys.maxsize else 'Poor KCM'


T = int(sys.stdin.readline())
for _ in range(T):
    N, M, K = map(int, sys.stdin.readline().split())
    graph = collections.defaultdict(list)
    for _ in range(K):
        u, v, c, d = map(int, sys.stdin.readline().split())
        graph[u].append((v, c, d))
        # graph[v].append((u,c,d))

    for i in range(1,N+1):
        graph[i].sort(key=lambda x:x[2])
    print(dijkstra())
