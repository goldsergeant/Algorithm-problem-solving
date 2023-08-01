import sys

input = sys.stdin.readline
v, e = map(int, input().split())
edges = []
parent = [0] + [i for i in range(1,v+1)]
answer=0

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    root_a = find(a)
    root_b = find(b)
    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b


for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find(a)!=find(b):
        union(a,b)
        answer+=cost

print(answer)
