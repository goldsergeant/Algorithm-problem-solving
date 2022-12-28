import collections
import heapq
import sys

V, E = map(int, input().split())
k = int(input())
graph = [[] for _ in range(V + 1)]
distance = [sys.maxsize] * (V + 1)
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

distance[k] = 0
queue = []
heapq.heappush(queue, [0, k])
while queue:
    cur_distance, cur_vertex = heapq.heappop(queue)
    if cur_distance > distance[cur_vertex]:
        continue

    for node in graph[cur_vertex]:
        d = node[1] + cur_distance
        if distance[node[0]] > d:
            distance[node[0]] = d
            heapq.heappush(queue, [d, node[0]])

for i in range(1, V + 1):
    print(distance[i] if distance[i] != sys.maxsize else 'INF')
