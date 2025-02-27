import collections
from heapq import heappush, heappop
import sys


def solution(n, start, end, roads, traps):
    def dijkstra():
        heap = [(0, start, 0)]
        distance = [[sys.maxsize for _ in range(1 << 10)] for _ in range(n + 1)]  # 일반일때, 밟은 트랩의 상태
        distance[start][0] = 0

        while heap:
            cost, node, visited_traps_bit = heappop(heap)

            if cost > distance[node][visited_traps_bit]:
                continue

            if is_trap_node[node]:
                trap_number = node_to_trap_number[node]
                trap_bit = 1 << trap_number
                if visited_traps_bit & trap_bit:  # 트랩으로 변경된 경우
                    for next_node, next_cost in changed_graph[node]:
                        n_visited_traps_bit = visited_traps_bit
                        if is_trap_node[next_node]:
                            next_trap_number = node_to_trap_number[next_node]
                            next_trap_bit = 1 << next_trap_number
                            if visited_traps_bit & next_trap_bit:  # 이미 다음 트랩도 밟은 경우엔 바뀐 길을 가면 안됨
                                continue
                            n_visited_traps_bit = visited_traps_bit | next_trap_bit
                        if cost + next_cost < distance[next_node][n_visited_traps_bit]:
                            distance[next_node][n_visited_traps_bit] = cost + next_cost
                            heappush(heap, (distance[next_node][n_visited_traps_bit], next_node, n_visited_traps_bit))
                    for next_node, next_cost in graph[node]:
                        if not is_trap_node[next_node]:  # 다음 노드가 트랩일 경우에만
                            continue
                        next_trap_number = node_to_trap_number[next_node]
                        next_trap_bit = 1 << next_trap_number
                        if not visited_traps_bit & next_trap_bit:  # 다음 트랩을 밟지 않았다면 원래 길로 갈 수 없음
                            continue
                        n_visited_traps_bit = visited_traps_bit ^ next_trap_bit
                        if cost + next_cost < distance[next_node][n_visited_traps_bit]:
                            distance[next_node][n_visited_traps_bit] = cost + next_cost
                            heappush(heap, (distance[next_node][n_visited_traps_bit], next_node, n_visited_traps_bit))

                else:  # 트랩으로 변경되지 않은 경우
                    for next_node, next_cost in graph[node]:
                        n_visited_traps_bit = visited_traps_bit
                        if is_trap_node[next_node]:
                            next_trap_number = node_to_trap_number[next_node]
                            next_trap_bit = 1 << next_trap_number
                            if visited_traps_bit & next_trap_bit:  # 다음 트랩을 밟은 경우는 갈 수 없음
                                continue
                            n_visited_traps_bit = visited_traps_bit | next_trap_bit
                        if cost + next_cost < distance[next_node][n_visited_traps_bit]:
                            distance[next_node][n_visited_traps_bit] = cost + next_cost
                            heappush(heap, (distance[next_node][n_visited_traps_bit], next_node, n_visited_traps_bit))

                    for next_node, next_cost in changed_graph[node]:
                        if not is_trap_node[next_node]:
                            continue
                        next_trap_number = node_to_trap_number[next_node]
                        next_trap_bit = 1 << next_trap_number
                        if not visited_traps_bit & next_trap_bit:  # 다음 트랩을 밟은 경우에만 갈 수 있음
                            continue
                        n_visited_traps_bit = visited_traps_bit ^ next_trap_bit
                        if cost + next_cost < distance[next_node][n_visited_traps_bit]:
                            distance[next_node][n_visited_traps_bit] = cost + next_cost
                            heappush(heap, (distance[next_node][n_visited_traps_bit], next_node, n_visited_traps_bit))
            else:
                for next_node, next_cost in graph[node]:
                    n_visited_traps_bit = visited_traps_bit
                    if is_trap_node[next_node]:
                        next_trap_number = node_to_trap_number[next_node]
                        next_trap_bit = 1 << next_trap_number
                        if visited_traps_bit & next_trap_bit:  # 이미 트랩을 밟은 경우
                            continue
                        n_visited_traps_bit = visited_traps_bit | next_trap_bit

                    if cost + next_cost < distance[next_node][n_visited_traps_bit]:
                        distance[next_node][n_visited_traps_bit] = cost + next_cost
                        heappush(heap, (distance[next_node][n_visited_traps_bit], next_node, n_visited_traps_bit))
                for next_node,next_cost in changed_graph[node]:
                    if not is_trap_node[next_node]:
                        continue
                    next_trap_number = node_to_trap_number[next_node]
                    next_trap_bit = 1 << next_trap_number
                    if not visited_traps_bit & next_trap_bit:
                        continue
                    n_visited_traps_bit=visited_traps_bit^next_trap_bit

                    if cost + next_cost < distance[next_node][n_visited_traps_bit]:
                        distance[next_node][n_visited_traps_bit] = cost + next_cost
                        heappush(heap, (distance[next_node][n_visited_traps_bit], next_node, n_visited_traps_bit))

        return distance

    answer = 0
    is_trap_node = [False for _ in range(n + 1)]
    node_to_trap_number = collections.defaultdict(int)
    trap_number_to_node = collections.defaultdict(int)
    graph = collections.defaultdict(list)
    changed_graph = collections.defaultdict(list)

    trap_number = 0
    for trap in traps:
        is_trap_node[trap] = True
        node_to_trap_number[trap] = trap_number
        trap_number_to_node[trap_number] = trap
        trap_number += 1

    for i in range(len(roads)):
        u, v, c = roads[i]
        graph[u].append((v, c))
        if is_trap_node[u] or is_trap_node[v]:
            changed_graph[v].append((u, c))

    return min(dijkstra()[end])
    # return answer


print(solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2]))
print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))
