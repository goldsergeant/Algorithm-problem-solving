import collections
import sys

n, q = map(int, input().split())
logs = [[0,0,0,0]] + [list(map(int, sys.stdin.readline().split()))+[i] for i in range(1,n+1)]
parent = [i for i in range(n + 1)]
questions = [list(map(int, sys.stdin.readline().split())) for _ in range(q)]


def find(x):
    if x == parent[x]:
        return x
    return find(parent[x])


def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        if logs[a][2] < logs[b][2]:
            parent[b] = a
        else:
            parent[a] = b


logs.sort()

for i in range(2, len(logs)):
    if logs[i-1][1]>=logs[i][0]:
        union(logs[i][3],logs[i-1][3])

for question in questions:
    one, two = question
    print(1 if find(one) == find(two) else 0)

