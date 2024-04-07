import sys
from math import log2, ceil


def query_seg(node, start, end, left, right):
    if start > right or end < left:
        return 0
    if left <= start and end <= right:
        return seg[node]

    mid = (start + end) // 2
    return query_seg(node * 2, start, mid, left, right) + query_seg(node * 2 + 1, mid + 1, end, left, right)


def update_seg(node, start, end, idx, val):
    if start > idx or end < idx:
        return seg[node]
    if start == end:
        seg[node] = val
        return seg[node]
    mid = (start + end) // 2
    seg[node] = update_seg(node * 2, start, mid, idx, val) + update_seg(node * 2 + 1, mid + 1, end, idx, val)
    return seg[node]
    # if start==end:
    #     seg[node]=val
    #     return
    # mid =(start+end)//2
    # if idx<=mid:
    #     update_seg(node*2,start,mid,idx,val)
    # else:
    #     update_seg(node*2+1,mid+1,end,idx,val)
    #
    # seg[node]=seg[node*2]+seg[node*2+1]


N = int(sys.stdin.readline())
numbers = []
for idx, num in enumerate(list(map(int, sys.stdin.readline().split()))):
    numbers.append((idx, num))
numbers.sort(key=lambda x: x[1])
h = ceil(log2(N)) + 1
node_cnt = 1 << h
seg = [0 for _ in range(node_cnt)]
answer = 0
for idx, num in numbers:
    answer += query_seg(1, 0, N - 1, idx + 1, N - 1)
    update_seg(1, 0, N - 1, idx, 1)

print(answer)
