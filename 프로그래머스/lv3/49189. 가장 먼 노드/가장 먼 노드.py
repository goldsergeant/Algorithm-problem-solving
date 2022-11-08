import collections
import sys
def solution(n, edge):
    graph = collections.defaultdict(list)
    visited = [0]*(n+1)
    visited[1]=1
    queue = collections.deque()
    queue.append(1)
    for i in edge:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])

    while queue:
        num = queue.popleft()
        for next_node in graph[num]:
            if visited[next_node]==0:
                visited[next_node] = visited[num] + 1
                queue.append(next_node)
    return visited.count(max(visited))
        