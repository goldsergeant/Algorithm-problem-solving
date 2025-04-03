import sys
import math
from heapq import heappush, heappop

T = int(sys.stdin.readline())
for _ in range(T):
    M = int(sys.stdin.readline())
    numbers = []
    for _ in range(math.ceil(M / 10)):
        numbers.extend(list(map(int, sys.stdin.readline().split())))

    max_heap = []
    min_heap = []
    answer = []

    for i, num in enumerate(numbers):
        if len(max_heap) == len(min_heap):
            heappush(max_heap, -num)
        else:
            heappush(min_heap, num)

        if min_heap and min_heap[0] < -max_heap[0]:
            big = -heappop(max_heap)
            small = heappop(min_heap)
            heappush(min_heap,big)
            heappush(max_heap, -small)
        if i%2==0:
            answer.append(-max_heap[0])

    print(len(answer))
    for i in range(len(answer)):
        print(answer[i], end=' ')
        if (i + 1) % 10 == 0 and i < len(answer) - 1:
            print()
    print()
