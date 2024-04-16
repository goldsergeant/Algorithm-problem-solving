import sys
from math import ceil,log2

def init_seg(node,start,end):
    if start==end:
        tree[node]=numbers[start]
        return tree[node]

    mid=(start+end)//2
    tree[node]=init_seg(node*2,start,mid)+init_seg(node*2+1,mid+1,end)
    return tree[node]

def query_seg(node,start,end,left,right):
    if start>right or end<left:
        return 0
    if left<=start and end<=right:
        return tree[node]

    mid=(start+end)//2
    return query_seg(node*2,start,mid,left,right)+query_seg(node*2+1,mid+1,end,left,right)

def update_seg(node,start,end,idx,val):
    if start>idx or end<idx:
        return tree[node]
    if start==end:
        tree[node]=val
        return tree[node]

    mid=(start+end)//2
    tree[node]=update_seg(node*2,start,mid,idx,val)+update_seg(node*2+1,mid+1,end,idx,val)
    return tree[node]

N,Q=map(int,sys.stdin.readline().split())
numbers=list(map(int,sys.stdin.readline().split()))
height=ceil(log2(N))+1
node_cnt=1<<height
tree=[0 for _ in range(node_cnt)]
init_seg(1,0,N-1)
for _ in range(Q):
    x,y,a,b=map(int,sys.stdin.readline().split())
    x,y=min(x,y),max(x,y)
    print(query_seg(1,0,N-1,x-1,y-1))
    update_seg(1,0,N-1,a-1,b)