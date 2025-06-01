import sys
sys.setrecursionlimit(10**7)

N = int(sys.stdin.readline())
K, P = map(int, sys.stdin.readline().split())
up_num = K + 1
down_num = K - 1
heap_num = 0
heap = [0 for _ in range(N + 1)]


def raise_exception():
    print(-1)
    exit()


def set_child(idx):
    global down_num
    if idx > N:
        return

    down_num += 1
    if down_num > N:
        raise_exception()

    heap[idx] = down_num
    set_child(idx * 2)
    set_child(idx * 2 + 1)


def set_parent(idx):
    global up_num
    if idx < 1:
        return
    up_num -= 1
    if up_num == 0:
        raise_exception()

    heap[idx] = up_num
    set_parent(idx // 2)


def up_heap(idx):
    if idx==1:
        return

    if heap[idx]>heap[idx//2]:
        heap[idx],heap[idx//2]=heap[idx//2],heap[idx]
        up_heap(idx//2)

def insert(idx):
    global heap_num
    if idx > N:
        return

    heap_num += 1
    if heap_num == up_num:
        heap_num = down_num + 1

    heap[idx] = heap_num
    insert(idx * 2)
    insert(idx * 2 + 1)


set_child(P)
set_parent(P)

for i in range(1, N + 1):
    if heap[i] == 0:
        insert(i)

print(*heap[1:],sep='\n')
