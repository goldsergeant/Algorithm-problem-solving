import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
lines = list(list(map(int, sys.stdin.readline().split())) for _ in range(M))
lines.sort(key=lambda x: x[2])
parent = [i for i in range(N + 1)]
answer = 0


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


for a, b, c in lines:
    if find(a)!=find(b):
        union(a, b)
        answer += c

print(answer)
