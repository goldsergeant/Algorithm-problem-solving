import sys
from math import ceil, log2

sys.setrecursionlimit(10 ** 7 + 1)
MOD_NUM = 1000000007

N, M, K = map(int, sys.stdin.readline().split())
numbers = list(int(sys.stdin.readline()) for _ in range(N))
height = ceil(log2(N)) + 1
node_cnt = 1 << height
seg = [0 for _ in range(node_cnt)]


def init_seg(node, left, right):
    if left == right:
        seg[node] = numbers[left]
        return seg[node]

    mid = (left + right) // 2
    seg[node]=init_seg(node*2, left, mid)*init_seg(node*2+1,mid+1,right)%MOD_NUM
    return seg[node]


def find_seg(node, left, right):
    if c < left or b > right:
        return 1
    if b<=left and right<=c:
        return seg[node]

    mid = (left + right) // 2
    return find_seg(node*2,left,mid)*find_seg(node*2+1,mid+1,right)%MOD_NUM

def update_seg(node, left, right, val):
    if left>b or right < b:
        return seg[node]
    if left == right:
        seg[node] = val
        return seg[node]

    mid = (left + right) // 2
    l=update_seg(node * 2, left, mid, val)
    r=update_seg(node * 2 + 1, mid + 1, right, val)
    seg[node]=(l*r)%MOD_NUM
    return seg[node]


init_seg(1, 0, len(numbers) - 1)

for _ in range(M + K):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        b -= 1
        update_seg(1, 0, len(numbers) - 1, c)
    elif a == 2:
        b -= 1
        c -= 1
        print(find_seg(1, 0,len(numbers)-1)%MOD_NUM)
