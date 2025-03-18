import collections
import sys
sys.setrecursionlimit(10000+1)

def dfs(node):
    visited[node]=True

    is_oosu=people[node]
    not_oosu=0
    for next_node in graph[node]:
        if not visited[next_node]:
            oosu,no_oosu=dfs(next_node)
            is_oosu+=no_oosu
            not_oosu+=max(oosu,no_oosu)

    return is_oosu,not_oosu

N=int(sys.stdin.readline())
people=[0]+list(map(int,sys.stdin.readline().split()))
graph=collections.defaultdict(list)
visited=[False for _ in range(N+1)]
for _ in range(N-1):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
print(max(dfs(1)))