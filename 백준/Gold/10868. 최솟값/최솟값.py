import sys
from math import ceil,log2

def init_seg(node,start,end):
    if start==end:
        tree[node]=numbers[start]
        return tree[node]
    mid=(start+end)//2
    tree[node]=min(init_seg(node*2,start,mid),init_seg(node*2+1,mid+1,end))
    return tree[node]

def query_seg(node,start,end,left,right):
    if start>right or end<left:
        return sys.maxsize
    if left<=start and end<=right:
        return tree[node]

    mid=(start+end)//2
    return min(query_seg(node*2,start,mid,left,right),query_seg(node*2+1,mid+1,end,left,right))

N,M=map(int,sys.stdin.readline().split())
numbers=list(int(sys.stdin.readline()) for _ in range(N))
height=ceil(log2(N))+1
node_cnt=1<<height
tree=[0 for _ in range(node_cnt)]
init_seg(1,0,N-1)
for _ in range(M):
    a,b=map(int,sys.stdin.readline().split())
    print(query_seg(1,0,N-1,a-1,b-1))