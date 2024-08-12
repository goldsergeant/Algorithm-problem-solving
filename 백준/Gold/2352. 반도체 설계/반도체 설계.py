import sys
from bisect import bisect_left

N=int(sys.stdin.readline())
to_port= [0] + list(map(int, sys.stdin.readline().split()))
arr=[to_port[1]]

for i in range(1,len(to_port)):
    if to_port[i]>arr[-1]:
        arr.append(to_port[i])
    else:
        idx=bisect_left(arr,to_port[i])
        arr[idx]=to_port[i]

print(len(arr))