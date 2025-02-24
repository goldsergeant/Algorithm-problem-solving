import collections
import sys
from heapq import heappush, heappop


def wolf_dijkstra():
    heap = [(0, 1, True)]
    distance = [[sys.maxsize,sys.maxsize] for _ in range(N + 1)]
    # distance[1][0] = 0
    distance[1][1] = 0

    while heap:
        cost, node, is_faster = heappop(heap)
        if cost > distance[node][is_faster]:
            continue
        for next_node, next_cost in graph[node]:
            if is_faster:
                if cost + next_cost // 2 < distance[next_node][not is_faster]:
                    distance[next_node][not is_faster] = cost + next_cost // 2
                    heappush(heap, (cost + next_cost // 2, next_node, not is_faster))
            else:
                if cost + next_cost * 2 < distance[next_node][not is_faster]:
                    distance[next_node][not is_faster] = cost + next_cost * 2
                    heappush(heap, (distance[next_node][not is_faster], next_node, not is_faster))

    return distance


def fox_dijkstra():
    heap = [(0, 1)]
    distance = [sys.maxsize for _ in range(N + 1)]
    distance[1] = 0

    while heap:
        cost, node = heappop(heap)
        if cost > distance[node]:
            continue
        for next_node, next_cost in graph[node]:
            if cost + next_cost < distance[next_node]:
                distance[next_node] = cost + next_cost
                heappush(heap, (distance[next_node], next_node))

    return distance


N, M = map(int, sys.stdin.readline().split())
graph = collections.defaultdict(list)
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c*2))
    graph[b].append((a, c*2))

wolf_distance=wolf_dijkstra()
fox_distance=fox_dijkstra()
answer=0
for i in range(2,N+1):
    if min(wolf_distance[i])>fox_distance[i]:
        answer+=1

print(answer)
