import collections
import sys

def set_level():
    q=collections.deque([1])
    visited = [False for _ in range(N + 1)]
    visited[1]=True

    while q:
        node=q.popleft()

        for child in tree[node]:
            if visited[child]:
                continue
            visited[child]=True
            level[child]=level[node]+1
            parent[child]=node
            q.append(child)


N=int(sys.stdin.readline())
tree=[[] for _ in range(N+1)]
parent=[i for i in range(N+1)]
level=[0 for _ in range(N+1)]
for _ in range(N-1):
    a,b=map(int,sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)
M=int(sys.stdin.readline())

set_level()
for _ in range(M):
    a,b=map(int,sys.stdin.readline().split())
    while level[a]>level[b]:
        a=parent[a]

    while level[b]>level[a]:
        b=parent[b]

    while a!=b:
        a=parent[a]
        b=parent[b]

    print(a)