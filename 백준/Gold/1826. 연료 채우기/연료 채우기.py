import sys
from heapq import heappush,heappop

N = int(sys.stdin.readline())
stations=sorted([list(map(int, sys.stdin.readline().split())) for _ in range(N)])
to_village_distance, cur_fuel = map(int, sys.stdin.readline().split())
stations.append([to_village_distance, 0])
answer=0
heap=[]
for point,fuel in stations:
    if cur_fuel>=to_village_distance:
        break

    while cur_fuel<point and heap:
        cur_fuel-=heappop(heap)
        answer+=1

    if cur_fuel<point:
        break
    heappush(heap,-fuel)

print(answer if cur_fuel>=to_village_distance else -1)