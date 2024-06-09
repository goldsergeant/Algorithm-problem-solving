import sys
from collections import defaultdict
from bisect import bisect_left,bisect_right

LEFT = 'L'
RIGHT = 'R'
UP = 'U'
DOWN = 'D'

N, M = map(int, sys.stdin.readline().split())
x_clover = defaultdict(list)
y_clover = defaultdict(list)

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    x_clover[x].append(y)
    y_clover[y].append(x)

for key,arr in x_clover.items():
    x_clover[key].sort()
for key,arr in y_clover.items():
    y_clover[key].sort()

commands = sys.stdin.readline().rstrip()

cur_x, cur_y = 0, 0
for cmd in commands:
    if cmd == LEFT:
        idx=bisect_left(y_clover[cur_y],cur_x)-1
        cur_x=y_clover[cur_y][idx]
    elif cmd == RIGHT:
        idx=bisect_right(y_clover[cur_y],cur_x)
        cur_x=y_clover[cur_y][idx]
    elif cmd == UP:
        idx=bisect_right(x_clover[cur_x],cur_y)
        cur_y=x_clover[cur_x][idx]
    elif cmd == DOWN:
        idx=bisect_left(x_clover[cur_x],cur_y)-1
        cur_y=x_clover[cur_x][idx]

print(cur_x, cur_y)
