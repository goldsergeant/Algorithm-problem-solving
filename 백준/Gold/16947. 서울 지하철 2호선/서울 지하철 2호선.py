import collections
import sys
sys.setrecursionlimit(100000)

N = int(input())
graph = collections.defaultdict(list)
is_cycle_node = [False for _ in range(N + 1)]
cycle=False
distance=[-1 for _ in range(N+1)]
visited = [False for _ in range(N + 1)]

for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(vertex,depth,path,start):
    global cycle

    if depth<=2:
        for node in graph[vertex]:
            if not visited[node]:
                visited[node]=True
                dfs(node,depth+1,path+[node],start)
                visited[node]=False
    else:
        for node in graph[vertex]:
            if not visited[node]:
                visited[node]=True
                dfs(node,depth+1,path+[node],start)
                visited[node]=False
            else:
                if node==start:
                    cycle=True
                    for i in path:
                        is_cycle_node[i]=True
                    return


def bfs():
    queue=collections.deque()

    for i in range(1,N+1):
        if is_cycle_node[i]:
            queue.append(i)
            distance[i]=0

    while queue:
        now=queue.popleft()

        for node in graph[now]:
            if distance[node]==-1:
                queue.append(node)
                distance[node]=distance[now]+1


for i in range(1, N + 1):  # 사이클 판별
    if cycle:
        break

    visited[i]=True
    dfs(i,1,[i],i)
    visited[i]=False

bfs()

print(*distance[1:])
