import collections
import sys

N, S, E, M = map(int, sys.stdin.readline().split())
edges = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
graph = collections.defaultdict(list)
earn = list(map(int, sys.stdin.readline().split()))
distance = [-sys.maxsize for _ in range(N)]

for a, b, c in edges:
    graph[a].append((b, c))


def can_arrive(start, end):
    q = collections.deque([start])
    visited = [False for _ in range(N)]
    visited[start] = True

    while q:
        node = q.popleft()
        if node==end:
            return True
        for adj_node,adj_dist in graph[node]:
            if not visited[adj_node]:
                visited[adj_node]=True
                q.append(adj_node)

    return False

def bellman_ford(start):
    # 시작 노드에 대해서 초기화
    distance[start] = earn[start]
    # 전체 v - 1번의 라운드(round)를 반복
    for i in range(N):
        # 매 반복마다 '모든 간선'을 확인한다.
        for j in range(len(edges)):
            cur_node = edges[j][0]
            next_node = edges[j][1]
            edge_cost = edges[j][2]
            if distance[cur_node] != -sys.maxsize and distance[next_node] < distance[cur_node] - edge_cost + earn[
                next_node]:
                distance[next_node] = distance[cur_node] - edge_cost + earn[next_node]
                if i == N - 1 and can_arrive(cur_node,E):
                    return "Gee"

    return distance[E] if distance[E] != -sys.maxsize else 'gg'

if not can_arrive(S,E):
    print('gg')
    exit()
print(bellman_ford(S))
