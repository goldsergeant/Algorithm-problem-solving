import sys
from heapq import heappush, heappop

N, M = map(int, sys.stdin.readline().split())
lights = [0] + list(map(int, sys.stdin.readline().split()))
answer = []
heap = []

for i in range(1, M + M-1):
    heappush(heap, (-lights[i], i))

for i in range(M,N-M+2):
    while heap and heap[0][1]<i-M+1:
        heappop(heap)
    if i+M-1<len(lights):
        heappush(heap,(-lights[i+M-1],i+M-1))
    answer.append(-heap[0][0])

print(*answer)