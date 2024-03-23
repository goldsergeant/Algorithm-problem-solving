import sys


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


while True:
    M, N = map(int, sys.stdin.readline().split())
    if M==0 and N==0:
        break

    edges = []
    parent = [i for i in range(M)]
    total_cost=0
    used_cost=0

    for _ in range(N):
        a, b, c = map(int, sys.stdin.readline().split())
        edges.append((a, b, c))
        total_cost+=c

    edges.sort(key=lambda x: x[2])
    for a, b, c in edges:
        p_a, p_b = find(a), find(b)
        if p_a != p_b:
            union(p_a, p_b)
            used_cost+=c

    print(total_cost-used_cost)
