import sys
from math import log2,ceil
sys.setrecursionlimit(100000)

def init_seg(node, start, end):
    if start==end:
        seg[node]=numbers[start]
        return

    mid=(start+end)//2
    init_seg(node*2,start,mid)
    init_seg(node*2+1,mid+1,end)

def query_seg(node,start,end,idx,val):
    if start>idx or end<idx:
        return 0
    val+=seg[node]

    if start==end:
        return val

    mid=(start+end)//2
    return query_seg(node*2,start,mid,idx,val)+query_seg(node*2+1,mid+1,end,idx,val)

def update_seg(node,start,end,left,right,val):
    if start>right or end<left:
        return
    if left<=start and right>=end:
        seg[node]+=val
        return

    mid=(start+end)//2
    update_seg(node*2,start,mid,left,right,val)
    update_seg(node*2+1,mid+1,end,left,right,val)


N=int(sys.stdin.readline())
numbers=list(map(int,sys.stdin.readline().split()))
M=int(sys.stdin.readline())
h=ceil(log2(N))+1
node_cnt=1<<h
seg=[0 for _ in range(node_cnt)]

init_seg(1,0,len(numbers)-1)

for _ in range(M):
    arr=list(map(int,sys.stdin.readline().split()))
    if arr[0]==1:
        i=arr[1]-1
        j=arr[2]-1
        k=arr[3]
        update_seg(1,0,N-1,i,j,k)
    elif arr[0]==2:
        i=arr[1]-1
        print(query_seg(1,0,N-1,i,0))