import sys
from math import ceil, log2

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
max_idx = numbers.index(max(numbers))
M = int(sys.stdin.readline())
h = ceil(log2(N)) + 1
node_cnt = 1 << h
seg = [0 for _ in range(node_cnt)]


def init_seg(node, start, end):
    if start == end:
        seg[node] = (numbers[start],start) # value,idx
        return seg[node]

    mid = (start + end) // 2
    l = init_seg(node * 2, start, mid)
    r = init_seg(node * 2 + 1, mid + 1, end)

    seg[node]=min(l,r)
    return seg[node]


def find_seg(node, start,end,left,right):
    if start>right or end<left:
        return sys.maxsize,sys.maxsize
    if left<=start and end<=right:
        return seg[node]

    mid = (start+end) // 2
    l = find_seg(node * 2, start, mid, left,right)
    r = find_seg(node * 2 + 1, mid+1,end, left,right)
    return min(l,r)


def update_seg(node, start, end, idx, val):
    if start > idx or end < idx:
        return seg[node]
    if start == end:
        seg[node]=(val,idx)
        return seg[node]

    mid = (start + end) // 2
    l = update_seg(node * 2, start, mid, idx, val)
    r = update_seg(node * 2 + 1, mid + 1, end, idx, val)

    seg[node]=min(l,r)
    return seg[node]


init_seg(1, 0, len(numbers) - 1)

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        update_seg(1,0,len(numbers)-1,b-1,c)
    else:
        print(find_seg(1, 0,len(numbers)-1,b-1,c-1)[1]+1)
