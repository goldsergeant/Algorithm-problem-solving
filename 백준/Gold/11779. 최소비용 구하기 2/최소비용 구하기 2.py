import collections
import sys
from heapq import heappop, heappush


def dijkstra(start_node):
    heap = [(0, start_node, [start_node])]
    distance[start_node] = 0

    while heap:
        cost, node, visited_nodes = heappop(heap)
        if cost > distance[node]:
            continue

        for next_node, next_cost in graph[node]:
            total = next_cost + cost
            if total < distance[next_node]:
                distance[next_node] = total
                path[next_node]=node
                heappush(heap, (total, next_node, visited_nodes + [next_node]))


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = collections.defaultdict(list)
distance = [sys.maxsize for _ in range(N + 1)]
path = [i for i in range(N+1)]

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))

start, end = map(int, sys.stdin.readline().split())
dijkstra(start)
print(distance[end])
answer=[]
cur=end
while cur!=start:
    answer.append(cur)
    cur=path[cur]

answer.append(start)
print(len(answer))
print(*answer[::-1])