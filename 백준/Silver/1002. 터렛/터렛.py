import math
import sys

T = int(sys.stdin.readline())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    distance = math.sqrt((abs(x2 - x1) ** 2) + (abs(y2 - y1) ** 2))
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    elif r2 + r1 < distance or abs(r2-r1)>distance:
        print(0)
    elif r2 + r1 == distance or abs(r2-r1)==distance:
        print(1)
    elif abs(r2 - r1) < distance < r2 + r1:
        print(2)
   