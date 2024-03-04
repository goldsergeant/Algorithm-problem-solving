import collections
import sys


def dfs(node):
    global edge_cnt
    visited[node]=True

    total=0
    for next_node in graph[node]:
        edge_cnt+=1
        if not visited[next_node]:
            total+=dfs(next_node)
    return total+1

test_case = 1
while True:
    N, M = map(int, sys.stdin.readline().split())
    graph = collections.defaultdict(list)

    if N == 0 and M == 0:
        break

    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False for _ in range(N + 1)]
    tree_cnt = 0
    for i in range(1, N + 1):
        if not visited[i]:
            edge_cnt = 0
            nodes=dfs(i)
            if nodes-1==edge_cnt//2:
                tree_cnt+=1

    answer = ''
    if tree_cnt == 0:
        answer = 'No trees.'
    elif tree_cnt == 1:
        answer = 'There is one tree.'
    else:
        answer = f'A forest of {tree_cnt} trees.'

    print(f'Case {test_case}: {answer}')
    test_case += 1
