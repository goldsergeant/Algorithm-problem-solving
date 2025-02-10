import collections


def solution(n, path, order):
    def init_topology(): # bfs로 0부터 순회해서 위상 정렬 상태를 만든다.
        q = collections.deque([0])
        visited = [False for _ in range(n)]
        visited[0] = True
        while q:
            node=q.popleft()
            for next_node in graph[node]:
                if not visited[next_node]:
                    in_degree[next_node]+=1
                    visited[next_node] = True
                    q.append(next_node)

    in_degree=[0 for _ in range(n)]
    graph=collections.defaultdict(list)
    visited_cnt=0
    for a,b in path:
        graph[a].append(b)
        graph[b].append(a)
    init_topology()

    for a,b in order:
        graph[a].append(b)
        in_degree[b]+=1

    q=collections.deque([0])

    while q:
        node=q.popleft()
        visited_cnt+=1
        for next_node in graph[node]:
            in_degree[next_node]-=1
            if in_degree[next_node]==0:
                q.append(next_node)

    return visited_cnt==n


print(solution(9, [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]], [[8, 5], [6, 7], [4, 1]]))

