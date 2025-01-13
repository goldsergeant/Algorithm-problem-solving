import collections
import sys
sys.setrecursionlimit(1000000)

N = int(sys.stdin.readline())
graph = collections.defaultdict(list)
how_many = [0 for _ in range(N + 1)]
for i in range(2, N + 1):
    words = sys.stdin.readline().split()
    kind, cnt, parent = words[0], int(words[1]), int(words[2])
    graph[parent].append(i)
    how_many[i] = cnt if kind == 'S' else -cnt


def dfs(node):
    tmp = how_many[node]
    for child in graph[node]:
        tmp += dfs(child)

    if tmp<0:
        tmp=0
    # print(f'{node} {tmp}')
    return tmp


print(dfs(1))
