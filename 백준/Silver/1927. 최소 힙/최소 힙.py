import heapq
import sys

n = int(input())
arr = []
for _ in range(n):
    x = int(sys.stdin.readline().rstrip())
    if x == 0:
        if arr:
            print(heapq.heappop(arr))
        else:
            print(0)
    else:
        heapq.heappush(arr, x)
