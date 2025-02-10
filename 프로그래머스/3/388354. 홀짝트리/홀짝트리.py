import collections
from collections import defaultdict


def solution(nodes, edges):
    answer = [0, 0]
    graph = defaultdict(list)
    visited = [False] * (1000000 + 1)

    def bfs(start):
        q = collections.deque([start])
        visited[start] = True
        is_holjjak = True
        holjjak_root_chance = 1

        is_reverse_holjjak = True
        reverse_holjjak_root_chance = 1

        while q:
            node = q.popleft()
            children_cnt_if_root = len(graph[node])
            children_cnt_if_not_root = len(graph[node]) - 1

            if (node + children_cnt_if_not_root) % 2 == 1:  # 노드와 노드 자식을 더한게 홀수면 홀짝노드가 아님
                if holjjak_root_chance:
                    holjjak_root_chance -= 1
                    if (node + children_cnt_if_root) % 2 == 1:
                        is_holjjak = False
                else:
                    is_holjjak = False

            if (node + children_cnt_if_not_root) % 2 == 0:  # 노드와 노드 자식을 더한게 짝수면 역홀짝노드가 아님
                if reverse_holjjak_root_chance:
                    reverse_holjjak_root_chance -= 1
                    if (node + children_cnt_if_root) % 2 == 0:
                        is_reverse_holjjak = False
                else:
                    is_reverse_holjjak = False

            for next_node in graph[node]:
                if not visited[next_node]:
                    visited[next_node] = True
                    q.append(next_node)

        if is_holjjak:
            if holjjak_root_chance:  # 루트가 없다면 그건 홀짝이 아닌거죠
                is_holjjak = False
        if is_reverse_holjjak:
            if reverse_holjjak_root_chance:
                is_reverse_holjjak = False

        return is_holjjak, is_reverse_holjjak

    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)

    for node in nodes:
        if not visited[node]:
            is_holjjak, is_reverse_holjjak = bfs(node)
            if is_holjjak:
                answer[0] += 1
            if is_reverse_holjjak:
                answer[1] += 1

    return answer


print(solution([11, 9, 3, 2, 4, 6], [[9, 11], [2, 3], [6, 3], [3, 4]]))
print(solution([9, 15, 14, 7, 6, 1, 2, 4, 5, 11, 8, 10],[[5, 14], [1, 4], [9, 11], [2, 15], [2, 5], [9, 7], [8, 1], [6, 4]]))