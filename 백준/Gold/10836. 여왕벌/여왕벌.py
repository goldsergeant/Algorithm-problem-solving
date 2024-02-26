import sys

M, N = map(int, sys.stdin.readline().split())
grow = [1 for _ in range(2 * M - 1)]

for _ in range(N):
    a, b, c = map(int, sys.stdin.readline().split())
    for i in range(a, a + b):
        grow[i] += 1
    for i in range(a + b, a + b + c):
        grow[i] += 2

for i in range(M - 1, -1, -1):
    print(*([grow[i]] + grow[M:]))

