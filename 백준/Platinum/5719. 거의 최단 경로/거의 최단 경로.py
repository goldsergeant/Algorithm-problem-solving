import collections
import sys
from heapq import heappush, heappop


def remove_shortest_path():
    visited=[False for _ in range(N)]
    def dfs(node):
        visited[node] = True
        for pre_edge_num, pre_node in pre[node]:
            can_go_edge[pre_edge_num] = False
            if not visited[pre_node]:
                dfs(pre_node)


    distance = [sys.maxsize for _ in range(N)]
    distance[S] = 0
    pre = [[] for _ in range(N)]

    q = [(0, S)]

    while q:
        dist, node = heappop(q)
        if dist > distance[node]:
            continue
        if node == D:
            continue
        for edge_num, next_node, next_dist in graph[node]:
            if dist + next_dist < distance[next_node]:
                pre[next_node] = [(edge_num, node)]
                distance[next_node] = dist + next_dist
                heappush(q, (dist + next_dist, next_node))
            elif dist + next_dist == distance[next_node]:
                pre[next_node].append((edge_num, node))

    dfs(D)


def get_second_shortest_cost():
    distance = [sys.maxsize for _ in range(N)]
    distance[S] = 0
    q = [(0, S, [])]

    while q:
        dist, node, path = heappop(q)
        if dist > distance[node]:
            continue
        if node == D:
            return dist

        for edge_num, next_node, next_dist in graph[node]:
            if dist + next_dist < distance[next_node] and can_go_edge[edge_num]:
                distance[next_node] = dist + next_dist
                heappush(q, (dist + next_dist, next_node, path + [edge_num]))
    return -1


while True:
    N, M = map(int, sys.stdin.readline().split())
    if N == 0 and M == 0:
        break

    S, D = map(int, sys.stdin.readline().split())
    graph = collections.defaultdict(list)
    can_go_edge = [True for _ in range(M)]

    for i in range(M):
        u, v, p = map(int, sys.stdin.readline().split())
        graph[u].append((i, v, p))

    remove_shortest_path()
    print(get_second_shortest_cost())
