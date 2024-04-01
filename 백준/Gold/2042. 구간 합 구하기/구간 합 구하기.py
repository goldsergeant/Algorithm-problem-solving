import sys
from math import log2, ceil

sys.setrecursionlimit(10 ** 6 + 1)

N, M, K = map(int, sys.stdin.readline().split())
numbers = list(int(sys.stdin.readline()) for _ in range(N))
h = ceil(log2(len(numbers))) + 1
node_cnt = 1 << h
seg = [0 for _ in range(node_cnt)]


def init_seg(node, start, end):
    if start == end:
        seg[node] = numbers[start]
        return seg[node]

    mid = (start + end) // 2
    left = init_seg(node * 2, start, mid)
    right = init_seg(node * 2 + 1, mid + 1, end)
    seg[node] = left + right
    return seg[node]


def find_seg(node, start, end):
    if start > c or end < b:
        return 0
    if b <= start and end <= c:
        return seg[node]

    mid = (start + end) // 2
    return find_seg(node * 2, start, mid) + find_seg(node * 2 + 1, mid + 1, end)


def update_seg(node, start, end, diff):
    if b < start or b > end:
        return

    seg[node] += diff
    if start != end:
        mid = (start + end) // 2
        update_seg(node * 2, start, mid, diff)
        update_seg(node * 2 + 1, mid + 1, end, diff)


init_seg(1, 0, len(numbers) - 1)

for _ in range(M + K):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        b -= 1
        diff = c - numbers[b]
        numbers[b]=c
        update_seg(1, 0, len(numbers) - 1, diff)
    elif a == 2:
        b -= 1
        c -= 1
        print(find_seg(1, 0, len(numbers) - 1))
