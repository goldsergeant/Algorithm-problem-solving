import sys
sys.setrecursionlimit(100000)

n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range(n + 1)]
def find(x):
    if x!=parent[x]:
        parent[x]=find(parent[x])
    return parent[x]

def union(a,b):
    a=find(a)
    b=find(b)
    if a<b:
        parent[b]=parent[a]
    else:
        parent[a]=parent[b]

for _ in range(m):
    cmd, a, b = map(int, sys.stdin.readline().split())
    if cmd == 0:
        union(a,b)
    else:
        print('YES' if find(a)==find(b) else 'NO')

