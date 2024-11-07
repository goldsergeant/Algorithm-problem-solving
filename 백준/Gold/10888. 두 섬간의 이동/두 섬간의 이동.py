import math
import sys

input = sys.stdin.readline


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
        connected_count[a] += connected_count[b]
    elif a > b:
        parent[a] = b
        connected_count[b] += connected_count[a]


def get_pairs_count(n):
    return n * (n - 1) // 2


def get_bridge_count(n):
    return (n * (n + 1) * (n - 1)) // 6


N = int(input())
parent = [i for i in range(N + 1)]
connected_count = [1 for _ in range(N + 1)]
pairs_count=0
bridge_count=0
for _ in range(N - 1):
    num = int(input())
    a=find(num)
    b=find(num+1)
    pairs_count-= get_pairs_count(connected_count[a])+get_pairs_count(connected_count[b])
    bridge_count-= get_bridge_count(connected_count[a])+get_bridge_count(connected_count[b])
    union(a,b)

    pairs_count+=get_pairs_count(connected_count[a])
    bridge_count+=get_bridge_count(connected_count[a])
    print(pairs_count,bridge_count)
