import sys
from math import ceil, log2

sys.setrecursionlimit(10 ** 6)

N, M = map(int, sys.stdin.readline().split())
numbers = list(int(sys.stdin.readline()) for _ in range(N))


def init_seg(idx, start, end):
    if start == end:
        seg[idx] = (numbers[start], numbers[end],)
        return seg[idx]

    mid = (start + end) // 2
    left = init_seg(idx * 2, start, mid)
    right = init_seg(idx * 2 + 1, mid + 1, end)

    seg[idx] = (min(left[0], right[0]), max(left[1], right[1]))
    return seg[idx]


def find_seg(idx, start, end):
    if range_end < start or range_start > end:
        return sys.maxsize, -sys.maxsize

    if range_start <= start and range_end >= end:
        return seg[idx]

    mid = (start + end) // 2
    left = find_seg(idx * 2, start, mid)
    right = find_seg(idx * 2 + 1, mid + 1, end)
    return min(left[0], right[0]), max(left[1], right[1])


h = ceil(log2(N)) + 1
node_cnt = 1 << h
seg = [0] * node_cnt
init_seg(1, 0, len(numbers) - 1)


for _ in range(M):
    range_start, range_end = map(int, sys.stdin.readline().split())
    range_start-=1
    range_end-=1
    res=find_seg(1,0,len(numbers) - 1)
    print(res[0],res[1])