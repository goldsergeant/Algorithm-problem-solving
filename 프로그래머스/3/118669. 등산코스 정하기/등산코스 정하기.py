import collections
import sys
from heapq import heappop,heappush

def solution(n, paths, gates, summits):

    is_summit=[False for _ in range(n+1)]
    for s in summits:
        is_summit[s]=True
    graph=collections.defaultdict(list)
    for u,v,c in paths:
        graph[u].append((v,c))
        graph[v].append((u,c))

    heap = []

    for g in gates:
        heappush(heap,(0,0,g))

    distance = [[sys.maxsize, sys.maxsize] for _ in range(n + 1)]
    target_intensity = sys.maxsize
    target_summit = sys.maxsize
    while heap:
        weight, visited_summit, node = heappop(heap)
        if is_summit[node]:
            if visited_summit:
                if target_intensity > weight:
                    target_intensity = weight
                    target_summit = visited_summit
                elif target_intensity == weight and target_summit > visited_summit:
                    target_summit = visited_summit
                continue
        if distance[node][bool(visited_summit)] < weight:
            continue
        for adj, adj_weight in graph[node]:
            n_weight = max(weight, adj_weight)
            if is_summit[adj]:
                if visited_summit:
                    continue
                else:
                    if distance[adj][1] > n_weight:
                        distance[adj][1] = n_weight
                        heappush(heap, (n_weight, adj, adj))
            else:
                if distance[adj][bool(visited_summit)] > n_weight:
                    distance[adj][bool(visited_summit)] = n_weight
                    heappush(heap, (n_weight, visited_summit, adj))

    return [target_summit,target_intensity]


print(solution(	6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))
print(
    solution(	7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4]))
