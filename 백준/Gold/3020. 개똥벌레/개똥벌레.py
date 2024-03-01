import collections
import sys
from bisect import bisect_right,bisect_left

N, H = map(int, sys.stdin.readline().split())
top = [0 for _ in range(500000+1)]
bottom = [0 for _ in range(500000+1)]
height_dict=collections.defaultdict(int)
for i in range(N):
    h=int(sys.stdin.readline())
    if i % 2 == 0:
        bottom.append(h)
    else:
        top.append(h)

top.sort()
bottom.sort()

for i in range(1,H+1):
    b=len(bottom)-bisect_left(bottom,i)

    t_target=H-i+1
    t=len(top)-bisect_left (top,t_target)
    height_dict[b+t]+=1

key=min(height_dict.keys())
print(key,height_dict[key])
