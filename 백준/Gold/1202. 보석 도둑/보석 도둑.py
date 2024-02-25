import sys
from heapq import heappop,heappush

JEWELRY_WEIGHT=0
JEWELRY_PRICE=1

N,K=map(int,sys.stdin.readline().split())
jewelry_arr=[tuple(map(int,sys.stdin.readline().split())) for _ in range(N)]
bag_weights=list(int(sys.stdin.readline()) for _ in range(K))
answer=0

jewelry_arr.sort(key=lambda x:(x[0],-x[1]))
bag_weights.sort()

heap = []
jewelry_idx=0
for weight in bag_weights:
    while jewelry_idx<N and jewelry_arr[jewelry_idx][JEWELRY_WEIGHT]<=weight:
        heappush(heap,(-jewelry_arr[jewelry_idx][JEWELRY_PRICE]))
        jewelry_idx+=1

    if heap:
        answer+=-heappop(heap)

print(answer)