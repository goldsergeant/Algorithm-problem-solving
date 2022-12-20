import collections

n, m, v = map(int, input().split())
graph = collections.defaultdict(list)
visited = []
dfsArr = []
bfsArr = []
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

def dfs(num):
    if num in visited:
        return
    visited.append(num)
    dfsArr.append(num)
    for i in range(len(graph[num])):
        dfs(graph[num][i])


def bfs(v):
    queue = [v]
    bfsArr.append(v)
    while len(queue) > 0:
        num = queue.pop(0)
        for node in graph[num]:
            if node not in bfsArr:
                bfsArr.append(node)
                queue.append(node)


dfs(v)
bfs(v)

print(' '.join(map(str, dfsArr)))
print(' '.join(map(str, bfsArr)))
