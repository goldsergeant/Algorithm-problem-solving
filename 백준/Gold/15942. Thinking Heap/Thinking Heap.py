import sys
sys.setrecursionlimit(10**7)

N = int(sys.stdin.readline())
K, P = map(int, sys.stdin.readline().split())
heap = [0 for _ in range(N + 1)]
upnum,downnum=K+1,K-1
heapnum=0

def raise_exception():
    print(-1)
    exit()

def set_child(idx):
    global downnum
    downnum+=1
    if downnum>N:
        raise_exception()

    heap[idx]=downnum
    if idx*2<=N:
        set_child(idx * 2)
    if idx*2+1<=N:
        set_child(idx * 2 + 1)

def set_parent(idx):
    global upnum
    upnum-=1
    if upnum==0:
        raise_exception()

    heap[idx]=upnum
    if idx//2>0:
        set_parent(idx//2)

def up_heap(idx):
    if idx==1:
        return

    if heap[idx]<heap[idx//2]:
        heap[idx],heap[idx//2]=heap[idx//2],heap[idx]
        up_heap(idx//2)

def insert(idx):
    global heapnum
    heapnum+=1
    if heapnum==upnum:
        heapnum=downnum+1

    heap[idx]=heapnum
    up_heap(idx)
    if idx*2<=N:
        insert(idx*2)
    if idx*2+1<=N:
        insert(idx*2 + 1)

set_child(P)
set_parent(P)
for i in range(1,N+1):
    if heap[i]==0:
        insert(i)
print(*heap[1:],sep='\n')