import collections
import sys

n, k = map(int, sys.stdin.readline().split())
distance = [[False for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(k):
    a, b = map(int, sys.stdin.readline().split())
    distance[a][b] = True

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if distance[i][k] and distance[k][j]:
                distance[i][j] = True

s = int(sys.stdin.readline())
for _ in range(s):
    a, b = map(int, sys.stdin.readline().split())
    if distance[a][b]:
        print(-1)
    elif distance[b][a]:
        print(1)
    else:
        print(0)
